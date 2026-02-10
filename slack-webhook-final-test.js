// Final test - Slack webhook with push protection disabled
// This pattern is KNOWN to trigger GitHub secret detection

// FAKE Slack Incoming Webhook URL - completely invalid
const SLACK_WEBHOOK_FINAL = "https://hooks.slack.com/services/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ba";

// FAKE Slack Bot Token - completely invalid  
const SLACK_BOT_FINAL = "xoxb-1357924680-1357924680135-zYxWvUtSrQpOnMlKjIhGfEdC";

// Both are fake test credentials
module.exports = { SLACK_WEBHOOK_FINAL, SLACK_BOT_FINAL };
