#[macro_use]
extern crate quick_error;
extern crate arraydeque;
extern crate battery;

use std::env;
use std::io::{self, Write};
use std::process::exit;
use std::thread::sleep;
use std::time::Duration;

use arraydeque::{ArrayDeque, Wrapping};
use battery::units::ratio::percent;
use battery::units::time::second;
use battery::Manager as BatteryManager;
use battery::State;

/// The time we'll sleep between each iteration of the main loop
const SLEEP_DURATION: Duration = Duration::from_secs(5);

const BATTERY_FULL: char = '';
const BATTERY_75: char = '';
const BATTERY_50: char = '';
const BATTERY_25: char = '';
const BATTERY_EMPTY: char = '';
const QUESTION: char = '';
const LIGHTNING: char = '';

quick_error! {
    /// An error type that wraps around the Battery and std::io error types
    #[derive(Debug)]
    pub enum ErrorWrapper {
        Battery(err: battery::Error) {
            from()
        }
        Io(err: io::Error) {
            from()
        }
    }
}

fn main() -> Result<(), ErrorWrapper> {
    let manager = BatteryManager::new()?;
    let mut batteries = manager.batteries()?;

    if is_check_flag() {
        exit(if batteries.count() == 0 { 1 } else { 0 })
    }

    let mut battery = batteries
        .next()
        .expect("No batteries found")
        .expect("Unable to acecess battery information");

    let stdout = io::stdout();
    let mut writer = stdout.lock();

    let mut times: ArrayDeque<[i32; 8], Wrapping> = ArrayDeque::new();

    loop {
        let state = battery.state();
        let charge_level = battery.state_of_charge().get::<percent>();
        let time = battery.time_to_full().or(battery.time_to_empty());

        let state_icon = get_state_icon(&state);
        let battery_icon = get_battery_icon(charge_level);

        let mut output: Vec<String> = Vec::new();

        if let Some(state_icon) = state_icon {
            output.push(state_icon.to_string());
        }

        output.push(format!("{} {:.0}%", battery_icon, charge_level));

        if let Some(time) = time {
            // Get the time left in seconds, and push it to the buffer
            let time_in_seconds = time.get::<second>() as i32;
            times.push_back(time_in_seconds);

            // Calculate the average value in the time buffer and add it to the
            // output vector.
            let average_time = times.iter().sum::<i32>() / times.iter().len() as i32;
            output.push(seconds_to_time_string(average_time));
        } else {
            times.clear();
        }

        writeln!(&mut writer, "{}", output.join(" "))?;

        sleep(SLEEP_DURATION);
        manager.refresh(&mut battery)?;
    }
}

/// Get a string in the form `(HH:MM:SS)`, given a number of seconds.
#[inline]
fn seconds_to_time_string(seconds: i32) -> String {
    let mut minutes = seconds / 60;
    let hours = minutes / 60;
    minutes %= 60;
    format!("({:02}:{:02})", hours, minutes)
}

/// Returns true if the "--check" cli argument is present.
#[inline]
fn is_check_flag() -> bool {
    let args: Vec<String> = env::args().collect();
    args.contains(&"--check".to_string())
}

/// Get the icon representation of the given charging state
#[inline]
fn get_state_icon(state: &State) -> Option<char> {
    match state {
        State::Unknown => Some(QUESTION),
        State::Charging => Some(LIGHTNING),
        _ => None,
    }
}

/// Get the icon representation of the given battery charge
#[inline]
fn get_battery_icon(charge_level: f32) -> char {
    if charge_level < 12.5 {
        BATTERY_EMPTY
    } else if charge_level < 37.5 {
        BATTERY_25
    } else if charge_level < 62.5 {
        BATTERY_50
    } else if charge_level < 87.5 {
        BATTERY_75
    } else {
        BATTERY_FULL
    }
}
