"""
⚠️ WARNING: THIS FILE CONTAINS FAKE SECRETS FOR TESTING PURPOSES ONLY ⚠️

This file is intentionally created to test GitHub Secret Scanning.
All credentials below are FAKE and will NOT work in any system.

DO NOT use these in production or for any real authentication.
"""

# FAKE AWS credentials - for secret scanning test only
# Using realistic patterns (but still completely fake)
config = {
    # FAKE AWS access key - realistic pattern but invalid
    "AWS_ACCESS_KEY_ID": "AKIATESTTESTTESTTEST",  # FAKE - for testing secret scanning
    "AWS_SECRET_ACCESS_KEY": "abcdef1234567890ABCDEFGHIJKLMNOPQRSTUVWX",  # FAKE - for testing

    # FAKE GitHub Personal Access Token - realistic pattern but invalid  
    "GITHUB_TOKEN": "ghp_abcdefghijklmnopqrstuvwxyz1234567890AB",  # FAKE - for testing

    # FAKE Stripe API key - realistic pattern but invalid
    "STRIPE_KEY": "sk_test_51ABCDEabcdefghijklmnopqrstuvwxyz1234567890ABCDEF",  # FAKE - for testing
    
    # FAKE SendGrid API key
    "SENDGRID_API_KEY": "SG.abcdefghijklmnopqrstuvw.1234567890abcdefghijklmnopqrstuvwxyzABCDEF"  # FAKE - for testing
}

# NOTE: All values above are intentionally fake and used only to trigger
# GitHub's secret scanning detection for testing purposes.
