import os
import sys

# Participant data with certificate filenames
PARTICIPANTS = [
    {"pr": 18, "github_id": "Medhansh-Anand", "full_name": "Medhansh Anand", "cert_name": "MedhanshAnand"},
    {"pr": 17, "github_id": "shanyuth", "full_name": "Shanyuth Reddy", "cert_name": "ShanyuthReddy"},
    {"pr": 16, "github_id": "vivektks", "full_name": "VIVEK TKS", "cert_name": "VivekTKS"},
    {"pr": 15, "github_id": "Devi-Sandeepya", "full_name": "Devi Sandeepya", "cert_name": "DeviSandeepya"},
    {"pr": 14, "github_id": "Shanvi-naripireddy", "full_name": "Shanvi Rishi", "cert_name": "ShanviRishi"},
    {"pr": 13, "github_id": "AakashAkolkar", "full_name": "Aakash Akolkar", "cert_name": "AakashAkolkar"},
    {"pr": 11, "github_id": "CharithReddy007", "full_name": "Charith Reddy", "cert_name": "CharithReddy"},
    {"pr": 10, "github_id": "shri-honeytha", "full_name": "Shri Honeytha Reddy", "cert_name": "ShriHoneythaReddy"},
    {"pr": 9, "github_id": "Praharshita23", "full_name": "Peddi Praharshita", "cert_name": "PeddiPraharshita"},
    {"pr": 1, "github_id": "CMB-i", "full_name": "Charvi Bayana", "cert_name": "CharviBayana"},
    {"pr": 12, "github_id": "GeetPacMan", "full_name": "Geetika Pachauri", "cert_name": "GeetikaPachauri"},
    {"pr": 8, "github_id": "AlekhyaNelabhotla", "full_name": "Alekhya Nelabhotla", "cert_name": "AlekhyaNelabhotla"},
    {"pr": 2, "github_id": "sanjana-goskonda", "full_name": "Sanjana Goskonda", "cert_name": "SanjanaGoskonda"},
    {"pr": 7, "github_id": "Somoru", "full_name": "Rangisetti Lakshmi Pavan", "cert_name": "RangisettiLakshmiPavan"},
    {"pr": 6, "github_id": "Fluorite985", "full_name": "Pranav Akkina", "cert_name": "PranavAkkina"},
    {"pr": 5, "github_id": "CrustyLox", "full_name": "Nareen Reddy Kommireddy", "cert_name": "NareenReddyKommireddy"},
    {"pr": 3, "github_id": "Whyneedaname-lol", "full_name": "Madhav Basur", "cert_name": "MadhavBasur"}
]

def create_project_folder(github_id):
    """Create project folder for participant."""
    folder_path = os.path.join("projects", f"{github_id}-chatbot")
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def create_participant_md(participant):
    """Create markdown file for participant."""
    content = f"""# BotGenesis Workshop – Participation Record

**Full Name:** {participant['full_name']}  
**GitHub Username:** [{participant['github_id']}](https://github.com/{participant['github_id']})  
**Bot Name:** chatbot  
**PR Number:** #{participant['pr']}  
**Certificate:** [Download PDF](../certs/{participant['cert_name']}.pdf)

✅ Participation verified by Enigma – The Computer Science Club.
"""
    
    file_path = os.path.join("participants", f"{participant['github_id']}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

def update_readme():
    """Update README.md with certificate verification instructions."""
    readme_content = """# BotGenesis Workshop

## ✅ Certificate Verification

To verify a certificate:

1. Visit the `/participants/` folder.
2. Open the file matching the participant's GitHub username.
3. You'll see their full name, GitHub handle, PR number, and a link to download their certificate.

## Project Structure

- `participants/`: Contains participation records and verification details
- `certs/`: Contains issued certificates (when available)

## Verification Checklist

All participants have:
- A .md file in `participants/`
- A valid certificate link pointing to `/certs/`
- All links open properly in GitHub preview
- README contains verification instructions
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

def main():
    """Main execution function."""
    # Create necessary directories
    os.makedirs("projects", exist_ok=True)
    os.makedirs("participants", exist_ok=True)
    os.makedirs("certs", exist_ok=True)
    
    # Process each participant
    for participant in PARTICIPANTS:
        print(f"Processing {participant['full_name']}...")
        create_project_folder(participant['github_id'])
        create_participant_md(participant)
    
    # Update README
    update_readme()
    print("\nSetup completed successfully!")

if __name__ == "__main__":
    main() 