css = """
<style>

:root {
    --primary-bg: #f8fafc;
    --sidebar-bg: #1e293b;
    --chat-user-bg: #3b82f6;
    --chat-bot-bg: #ffffff;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --text-light: #ffffff;
    --border-color: #e2e8f0;
    --shadow-color: rgba(0, 0, 0, 0.1);
    --accent-color: #3b82f6;
}

/* Global Streamlit Overrides */
.stApp {
    background-color: var(--primary-bg);
}

.stSidebar {
    background-color: var(--sidebar-bg);
}

.stSidebar [data-testid="stSidebarNav"] {
    background-color: var(--sidebar-bg);
}

/* Sidebar Styling */
.stSidebar {
    padding: 2rem 1rem;
}

/* Make sidebar text lighter */
.stSidebar .stMarkdown h3,
.stSidebar .stMarkdown p,
.stSidebar [data-testid="stMarkdownContainer"] p,
.stSidebar [data-testid="stMarkdownContainer"] h3 {
    color: #e2e8f0 !important;
}

/* File Uploader Styling */
[data-testid="stFileUploader"] {
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 0.75rem;
    padding: 1.5rem;
    border: 2px dashed rgba(255, 255, 255, 0.2);
}

/* Chat Message Styling */
.chat-message {
    padding: 1.5rem;
    border-radius: 1rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: flex-start;
    box-shadow: 0 4px 6px var(--shadow-color);
    transition: transform 0.2s ease;
}

.chat-message:hover {
    transform: translateY(-2px);
}

.chat-message.user {
    background-color: var(--chat-user-bg);
    margin-left: 2rem;
}

.chat-message.bot {
    background-color: var(--chat-bot-bg);
    margin-right: 2rem;
    border: 1px solid var(--border-color);
}

.chat-message .avatar {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    font-size: 1.5rem;
    margin-right: 1rem;
    flex-shrink: 0;
}

.chat-message.bot .avatar {
    background-color: #e2e8f0;
}

.chat-message.user .avatar {
    background-color: rgba(255, 255, 255, 0.2);
}

.chat-message .message {
    flex-grow: 1;
    padding: 0 1rem;
}

.chat-message.user .message {
    color: var(--text-light);
}

.chat-message.bot .message {
    color: var(--text-primary);
}

/* Input and Button Styling */
[data-testid="stTextInput"] > div > div > input {
    background-color: white;
    border-radius: 0.5rem;
    border: 1px solid var(--border-color);
    padding: 0 1.5rem !important;
    height: 2.5rem !important;
    font-size: 1rem;
    box-shadow: 0 2px 4px var(--shadow-color);
    transition: all 0.2s ease;
    line-height: 3.5rem !important;
}

/* Fix placeholder vertical alignment */
[data-testid="stTextInput"] > div > div > input::placeholder {
    line-height: 3.5rem !important;
    vertical-align: middle;
}

[data-testid="stTextInput"] > div > div > input:focus {
    border-color: var(--accent-color);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

.stButton > button {
    background-color: var(--accent-color) !important;
    color: white !important;
    border-radius: 0.75rem !important;
    padding: 0.1rem 2rem !important;
    font-weight: 600 !important;
    border: none !important;
    transition: all 0.2s ease !important;
    margin-top: 27px !important;
    height: auto;
    width: auto;
}
.stButton > button:hover {
    background-color: #2563eb !important;
    transform: translateY(-2px);
}

/* Success/Error Message Styling */
.stSuccess, .stError, .stWarning, .stInfo {
    border-radius: 0.75rem;
    padding: 1rem 1.5rem;
    margin: 1rem 0;
    border: none;
    box-shadow: 0 2px 4px var(--shadow-color);
}

/* Additional Streamlit Element Styling */
.stProgress > div > div > div > div {
    background-color: var(--accent-color);
}

[data-testid="stHeader"] {
    background-color: transparent;
}

/* Markdown Content Styling */
.stMarkdown {
    color: var(--text-primary);
}

.element-container:has(.stMarkdown h3) {
    margin-top: 2rem;
}
</style>
"""
bot_template = """
<div class="chat-message bot">
    <div class="avatar">🤖
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""
user_template = """
<div class="chat-message user">
    <div class="avatar">👤
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""
