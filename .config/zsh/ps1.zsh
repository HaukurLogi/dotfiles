# Reset the terminal color
col_reset() {
    echo "%f"
}

# Set a color, if it already exists add a separator
set_color() {
    local fg="$1"
    CURRENT_COL="%F{$fg}"
}

# Current directory structure
current_path() {
    # Actually one less
    local max_dir_len=15
    local max_dirs=3

    # Get current path
    local pwd=$(pwd)
    local output_path=""
    if [[ "$(pwd)" == "/home/$USER"* ]]; then
        local pwd=$(echo $pwd | sed 's/^\/home\/'$USER'//')
        local output_path="~"
    fi

    # Convert path to an array
    local array=("${(ps:/:)pwd}")

    # Shorten each element in the list
    local short_array=()
    for elem in "${array[@]}"; do
        local short_elem=$(echo $elem | head -c $max_dir_len | sed 's/./…/'$max_dir_len)
        short_array+=("$short_elem")
    done

    # Take only the last $max_dirs elements
    if [[ "$((${#short_array[@]} - 1))" -gt "$max_dirs" ]]; then
        local offset=$((${#short_array[@]} - $max_dirs))
        local short_array=("${short_array[@]:$offset:$max_dirs}")
        output_path+="/…/"
    fi

    # Reconstruct the path from the shortened list
    function join_by { local IFS="$1"; shift; echo "$*"; }
    local joined_array=$(join_by "/" "${short_array[@]}")
    local output_path="$output_path$joined_array"

    set_color "blue"
    CURRENT_PATH="$(echo $CURRENT_COL$output_path$(col_reset))"
}

# Current version control status
vcs() {
    # Exit if not in git dir
    if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) != 'true' ]]; then
        return
    fi

    # Set branch name
    local branch=$(git symbolic-ref --short HEAD 2> /dev/null)

    # Get color based on directory status
    if [[ -n $(git status --porcelain) ]]; then
        set_color "red" # Changed -> Red
    else
        set_color "green" # Unchanged -> Green
    fi

    # Check if there is new stuff to commit
    if [[ -n $(git rev-list "$branch"@{upstream}..HEAD 2> /dev/null) ]]; then
        local push=" ↑"
    fi

    VCS="$(echo $CURRENT_COL$branch$push$(col_reset))"

    if [[ "$VCS" != "" ]]; then
        VCS="[$VCS]"
    fi
}

# Current user
current_user() {
    set_color "green"
    if [[ "$USER" == "root" ]]; then
        CURRENT_USER="$(echo $CURRENT_COLROOT$(col_reset))"
    else
        CURRENT_USER="$(echo $CURRENT_COL$USER$(col_reset))"
    fi
}

function precmd {
    # Export variables
    current_user
    current_path
    vcs

    PS1="[$CURRENT_USER][$CURRENT_PATH]$VCS%% "

    # Unset all variables
    unset CURRENT_USER
    unset CURRENT_PATH
    unset VCS
    unset CURRENT_COL

    unset col_reset
    unset blink
}
