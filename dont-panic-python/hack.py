from cs50 import SQL

# Connect to the database
db = SQL("sqlite:///dont-panic.db")

try:
    # Prompt the user for a new password
    new_password = input("Enter a new password for the administrator: ")

    # Check if the password input is not empty
    if new_password:
        # Update the administrator's password using a prepared statement
        db.execute(
            """
            UPDATE "users"
            SET "password" = ?
            WHERE "username" = 'admin';
            """,
            new_password
        )

        # Inform the user that the hack is complete
        print("Administrator's password has been updated successfully!")
    else:
        print("No password entered. The password has not been changed.")

except Exception as e:
    print(f"An error occurred: {e}")
