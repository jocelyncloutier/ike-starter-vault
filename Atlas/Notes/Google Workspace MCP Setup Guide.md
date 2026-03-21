---
created: 2026-03-21
authorship: ai-generated
map: ["[[Getting Started Map]]"]
tags:
  - topic/ike
  - topic/mcp
---

## What This Gives You

Google Workspace MCP connects Claude to your Google account. Once set up, you can ask Claude to:
- Read, search, draft, and send **Gmail** messages
- Check your **Calendar**, create events, find free time
- Read, create, and edit **Google Docs**
- Create and edit **Google Slides** presentations
- Search and organize **Google Drive** files
- Read and update **Google Sheets**
- Create **Google Forms** and view responses
- Search and manage **Google Contacts**
- Send and read **Google Chat** messages
- Manage **Google Tasks**

Everything happens through conversation — no need to switch apps.

## Setup Steps
### Step 1 — Install Claude Desktop

If you haven't already, download and install Claude Desktop from [claude.com/download](https://claude.com/download). Launch it and sign in to your Claude account.
### Step 2 — Open Claude Desktop Settings

Click your profile icon in the bottom-left corner of Claude Desktop.

![[Pasted image 20260321091014.png|260]]

Select **Settings**.
### Step 3 — Go to Connectors

In Settings, click **Connectors**.

![[Pasted image 20260321091109.png|320]]
### Step 4 — Go to Customize

At the top of the Connectors screen, click **Go to customize**.

![[Pasted image 20260321091142.png|600]]
### Step 5 — Add a Custom Connector

Click the **+** (plus sign) button.

![[Pasted image 20260321091217.png|600]]

Click **Add custom connector**.

![[Pasted image 20260321091242.png|320]]

Fill in the details:
- **Name:** `Google Workspace (IKE)`
- **URL:** `https://workspace-mcp-866172746429.us-central1.run.app/mcp`

![[Pasted image 20260321091334.png|600]]

Click **Add**.
### Step 6 — Connect and Authenticate

After adding, you'll see the new connector in the list.

![[Pasted image 20260321091550.png|320]]

Click on it, then click **Connect**.

![[Pasted image 20260321091621.png|600]]

Your web browser will open. Select your Google account and approve the permissions.
* Select your google accounts (it is required)

![[Pasted image 20260321091657.png|600]]

There are 2 approval steps in the browser. When done, Claude Desktop reopens showing the connector as connected.

![[Pasted image 20260321101400.png|600]]
### Step 7 — Test It

Open a new chat in Claude Desktop and type: **"What is the subject of my most recent Gmail email?"**

![[Pasted image 20260321091844.png|320]]

The first connection takes about 20 seconds. You may see a permission prompt — select **Allow once** or **Always allow** to let Claude access your Gmail.

![[Pasted image 20260321091954.png|500]]

If Claude returns real data, you're set.
### Step 8 — Configure Permissions (Optional)

Go back to **Settings → Connectors** and click **Configure** on the Google Workspace (IKE) connector.

![[Pasted image 20260321092129.png|500]]

This is where you control tool permissions. We recommend selecting **Always allow** for most tools so Claude doesn't ask for permission on every request.

![[Pasted image 20260321092212.png|500]]
## Using Google Workspace in Claudian

The connector you just set up works everywhere — Claude Desktop, Claudian (Obsidian sidebar), and Claude Code CLI. They all share the same credentials.

Claudian is pinned in the right sidebar by default. If you closed it, you can reopen it two ways:
- Click the Claudian icon in the ribbon (left edge)
  |![[Pasted image 20260321093053.png|320]]
- Press **Cmd+P** to open the command palette, type `Claudian`, and select **Open chat view**
  ![[Pasted image 20260321093752.png|500]]
Try these:
- **"What's on my calendar today?"**
- **"Draft an email to [person] about [topic]"**
- **"Find my Google Doc about [topic]"**
## Re-authentication

Google tokens expire every 7 days. When this happens, Claude Desktop will automatically prompt you to re-authenticate from the chat — just follow the sign-in flow when prompted.

If the automatic prompt doesn't appear, you can manually re-authenticate:
1. Go to Claude Desktop → **Settings** → **Connectors**
2. Find "Google Workspace (IKE)" and **disconnect** it
3. **Reconnect** it — this triggers a fresh Google sign-in
4. After sign-in, the connection is restored everywhere (Claudian, Claude Code CLI, Claude Desktop)
## Privacy and Security

- **Your data stays between you and Google.** Claude sends requests to Google's APIs on your behalf using your authenticated session. No Google data is stored on the MCP server.
- **Each user has their own session.** No one else can see your emails, calendar, or files. The server keeps sessions separate by Google account.
- **You can disconnect anytime.** Remove the connector in Claude Desktop Settings → Connectors to revoke access.
## Note About MCP Server Approval

The first time you open Claudian or Claude Code in your IKE vault, you may see:

> "New MCP server found: google-workspace. Allow?"

Select **Yes**. This is a separate approval from the connector setup above — it tells Claude Code to use the Google Workspace server that's pre-configured in your vault. If you've already set up the connector, tools will work immediately after approving.
## Related

- [[When to Use What]] — examples of what to ask Claude with Google Workspace
- [[Getting Started]] — vault orientation
