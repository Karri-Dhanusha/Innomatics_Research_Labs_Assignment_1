# Define the log level to track
LOG_LEVEL_TO_TRACK = "ERROR"


def count_log_entries(logs, log_level):
    """
    Counts the occurrences of a specific log level in the logs list.
    
    Args:
        logs (list): List of log entries
        log_level (str): The log level to count
        
    Returns:
        int: Number of occurrences of the specified log level
    """
    return logs.count(log_level)


def main():
    """Main function to analyze and display log statistics."""
    log_entries = ["INFO", "ERROR", "WARNING", "ERROR"]
    
    error_count = count_log_entries(log_entries, LOG_LEVEL_TO_TRACK)
    
    print(f"Total {LOG_LEVEL_TO_TRACK} entries: {error_count}")


if __name__ == "__main__":
    main()
