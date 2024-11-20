#!/bin/bash

# File Management and Nano Editing Script

# Function to display menu
show_menu() {
    echo "File Management and Editing Menu"
    echo "--------------------------------"
    echo "1. Create a new file"
    echo "2. Open file in nano"
    echo "3. List files in current directory"
    echo "4. Delete a file"
    echo "5. Exit"
}

# Function to create a file
create_file() {
    read -p "Enter the filename you want to create: " filename
    
    # Check if filename is empty
    if [ -z "$filename" ]; then
        echo "Filename cannot be empty!"
        return
    }
    
    # Use touch to create the file
    touch "$filename"
    
    if [ $? -eq 0 ]; then
        echo "File '$filename' created successfully!"
    else
        echo "Failed to create file '$filename'"
    fi
}

# Function to open file in nano
open_file() {
    read -p "Enter the filename you want to open: " filename
    
    # Check if filename is empty
    if [ -z "$filename" ]; then
        echo "Filename cannot be empty!"
        return
    }
    
    # Check if file exists
    if [ ! -f "$filename" ]; then
        echo "File '$filename' does not exist!"
        return
    }
    
    # Open file in nano
    nano "$filename"
}

# Function to list files
list_files() {
    echo "Files in the current directory:"
    ls -l
}

# Function to delete a file
delete_file() {
    read -p "Enter the filename you want to delete: " filename
    
    # Check if filename is empty
    if [ -z "$filename" ]; then
        echo "Filename cannot be empty!"
        return
    }
    
    # Check if file exists
    if [ ! -f "$filename" ]; then
        echo "File '$filename' does not exist!"
        return
    }
    
    # Confirm deletion
    read -p "Are you sure you want to delete '$filename'? (y/n): " confirm
    
    if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
        rm "$filename"
        if [ $? -eq 0 ]; then
            echo "File '$filename' deleted successfully!"
        else
            echo "Failed to delete file '$filename'"
        fi
    else
        echo "Deletion cancelled."
    fi
}

# Main script loop
while true; do
    show_menu
    
    read -p "Enter your choice (1-5): " choice
    
    case $choice in
        1) create_file ;;
        2) open_file ;;
        3) list_files ;;
        4) delete_file ;;
        5) 
            echo "Exiting script. Goodbye!"
            exit 0
            ;;
        *) 
            echo "Invalid option. Please enter a number between 1 and 5."
            ;;
    esac
    
    # Add a pause to see the result
    read -n 1 -s -r -p "Press any key to continue..."
    clear
done
