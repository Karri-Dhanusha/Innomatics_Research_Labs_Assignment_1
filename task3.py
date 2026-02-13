def clean_names(names):
    """
    Cleans a list of names by stripping whitespace and converting to lowercase.
    
    Args:
        names (list): List of names to clean
        
    Returns:
        list: List of cleaned names
    """
    return [name.strip().lower() for name in names]


def main():
    """Main function to process and display cleaned names."""
    raw_names = [" Alice ", "bob", " CHARLIE "]
    
    cleaned_names = clean_names(raw_names)
    
    print(f"Cleaned Names: {cleaned_names}")


if __name__ == "__main__":
    main()