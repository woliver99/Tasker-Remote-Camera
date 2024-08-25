import sys
import segno

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Error: Missing required arguments.")
        print("Usage: python generate_qr.py <file_location> <text>")
        sys.exit(1)

    # Assign command-line arguments to variables
    file_location = sys.argv[1]
    text = sys.argv[2]

    # Generate and save the QR code
    qrcode = segno.make(text)
    qrcode.save(file_location)
    print(f"QR code saved to {file_location}")

if __name__ == "__main__":
    main()
