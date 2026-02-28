<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equinox | Wealth & Advisory AI</title>
    
    <!-- Distinctive Typography: Syne for premium display, DM Sans for crisp data readability -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Phosphor Icons for a sharp, technical look -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>

    <style>
        /* --- CSS VARIABLES & THEME --- */
        :root {
            /* Palette: Obsidian & Emerald (Fintech Premium) */
            --bg-base: #030404;
            --bg-surface: #0a0b0b;
            --bg-elevated: #111312;
            --bg-glass: rgba(17, 19, 18, 0.7);
            
            --text-main: #F4F5F4;
            --text-secondary: #A3A6A5;
            --text-muted: #5C615F;
            
            /* Emerald/Mint Accent for Finance */
            --accent-primary: #00E599; 
            --accent-glow: rgba(0, 229, 153, 0.12);
            --accent-muted: #00B377;
            
            --border-subtle: #1a1d1c;
            --border-highlight: rgba(255, 255, 255, 0.08);
            
            --font-display: 'Syne', sans-serif;
            --font-body: 'DM Sans', sans-serif;
            
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 24px;
            --radius-pill: 99px;
            
            --transition-snappy: 0.2s cubic-bezier(0.25, 1, 0.5, 1);
            --transition-smooth: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* --- RESET & BASE --- */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-body);
            background-color: var(--bg-base);
            color: var(--text-main);
            height: 100vh;
            overflow: hidden;
            display: flex;
            -webkit-font-smoothing: antialiased;
            background-image: 
                radial-gradient(circle at 10% 40%, rgba(255,255,255,0.015), transparent 30%),
                radial-gradient(circle at 90% 60%, rgba(0, 229, 153, 0.025), transparent 30%);
        }

        /* Subtle noise texture for premium, secure banking feel */
        body::before {
            content: "";
            position: absolute;
            inset: 0;
            z-index: -1;
            opacity: 0.035;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        }

        button {
            background: none;
            border: none;
            color: inherit;
            cursor: pointer;
            font-family: inherit;
        }

        input, textarea {
            font-family: inherit;
            outline: none;
        }

        /* --- LAYOUT --- */
        #app {
            display: flex;
            width: 100%;
            height: 100%;
        }

        /* --- SIDEBAR --- */
        .sidebar {
            width: 280px;
            background-color: var(--bg-surface);
            border-right: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            padding: 24px 16px;
            position: relative;
            z-index: 10;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 0 8px;
            margin-bottom: 32px;
        }

        .brand-logo {
            width: 32px;
            height: 32px;
            background: var(--text-main);
            border-radius: var(--radius-sm);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--bg-base);
        }

        .brand-name {
            font-family: var(--font-display);
            font-weight: 700;
            font-size: 1.25rem;
            letter-spacing: -0.02em;
        }

        .btn-new-chat {
            background-color: transparent;
            border: 1px solid var(--border-highlight);
            color: var(--text-main);
            padding: 14px;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.95rem;
            font-weight: 500;
            transition: var(--transition-snappy);
            position: relative;
            overflow: hidden;
        }

        .btn-new-chat::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(90deg, transparent, var(--accent-glow), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s ease;
        }

        .btn-new-chat:hover {
            border-color: var(--accent-primary);
            box-shadow: 0 0 15px var(--accent-glow);
        }

        .btn-new-chat:hover::before {
            transform: translateX(100%);
        }

        .btn-new-chat i {
            color: var(--accent-primary);
        }

        .history-section {
            margin-top: 32px;
            flex: 1;
            overflow-y: auto;
        }

        .history-section::-webkit-scrollbar { width: 4px; }
        .history-section::-webkit-scrollbar-thumb {
            background: var(--border-subtle);
            border-radius: 4px;
        }

        .history-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 12px;
            padding: 0 8px;
            font-weight: 600;
        }

        .history-item {
            padding: 10px 12px;
            margin: 2px 0;
            border-radius: var(--radius-sm);
            color: var(--text-secondary);
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: var(--transition-snappy);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            width: 100%;
        }

        .history-item:hover, .history-item.active {
            background-color: var(--bg-elevated);
            color: var(--text-main);
        }

        /* Sidebar Profile Block */
        .user-widget {
            margin-top: auto;
            padding: 12px;
            border-radius: var(--radius-md);
            background-color: var(--bg-elevated);
            border: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            transition: var(--transition-snappy);
        }

        .user-widget:hover {
            border-color: var(--border-highlight);
        }

        .avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: url('https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=100&auto=format&fit=crop') center/cover;
        }

        .user-info {
            flex: 1;
            overflow: hidden;
        }

        .user-name {
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-main);
        }

        .user-plan {
            font-size: 0.75rem;
            color: var(--accent-primary);
            font-weight: 500;
        }

        /* --- MAIN AREA --- */
        .main-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        /* Top Bar */
        .top-bar {
            height: 72px;
            padding: 0 32px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: absolute;
            top: 0; left: 0; right: 0;
            z-index: 20;
            background: linear-gradient(to bottom, var(--bg-base) 60%, transparent);
        }

        .model-selector {
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-display);
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
        }

        .model-selector i { color: var(--text-muted); }

        .login-btn-top {
            background: var(--bg-elevated);
            border: 1px solid var(--border-highlight);
            padding: 8px 16px;
            border-radius: var(--radius-pill);
            font-size: 0.85rem;
            font-weight: 600;
            transition: var(--transition-snappy);
        }
        .login-btn-top:hover {
            background: var(--text-main);
            color: var(--bg-base);
        }

        /* Chat View */
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 100px 20% 140px 20%;
            display: flex;
            flex-direction: column;
            gap: 40px;
            scroll-behavior: smooth;
        }

        .chat-container::-webkit-scrollbar { display: none; }

        .message {
            display: flex;
            gap: 20px;
            max-width: 100%;
            animation: fadeIn 0.5s ease forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .message-avatar {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .message.user .message-avatar {
            background: var(--bg-elevated);
            border: 1px solid var(--border-highlight);
        }

        .message.ai .message-avatar {
            background: var(--accent-primary);
            color: var(--bg-base);
        }

        .message-content {
            flex: 1;
            line-height: 1.6;
            color: var(--text-main);
            font-size: 1rem;
        }

        .message.user .message-content {
            color: var(--text-secondary);
        }

        /* Finance Component Block */
        .finance-block {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            overflow: hidden;
            margin-top: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .finance-header {
            padding: 16px;
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .finance-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--accent-primary);
            background: var(--accent-glow);
            padding: 6px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-family: var(--font-display);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-size: 0.7rem;
        }

        .finance-body {
            padding: 24px;
        }

        .finance-total {
            font-family: var(--font-display);
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 4px;
            letter-spacing: -0.02em;
        }
        
        .finance-subtitle {
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-bottom: 24px;
        }

        .budget-row {
            margin-bottom: 16px;
        }
        
        .budget-row:last-child {
            margin-bottom: 0;
        }

        .budget-labels {
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .budget-val { color: var(--text-secondary); }

        .bar-container {
            height: 8px;
            background: var(--bg-elevated);
            border-radius: 4px;
            overflow: hidden;
            border: 1px solid var(--border-subtle);
        }

        .bar-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 1s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .fill-needs { background: var(--accent-primary); width: 50%; }
        .fill-wants { background: #3B82F6; width: 30%; }
        .fill-savings { background: #8B5CF6; width: 20%; }

        .finance-footer {
            padding: 12px 16px;
            border-top: 1px solid var(--border-subtle);
            background: var(--bg-elevated);
            display: flex;
            gap: 12px;
        }

        .btn-action {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.85rem;
            color: var(--text-main);
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            transition: var(--transition-snappy);
        }
        .btn-action:hover {
            border-color: var(--border-highlight);
            background: var(--bg-base);
        }

        /* Input Area */
        .input-wrapper {
            position: absolute;
            bottom: 40px;
            left: 20%;
            right: 20%;
            z-index: 30;
        }

        .input-box {
            background: var(--bg-glass);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-lg);
            padding: 12px 16px;
            display: flex;
            align-items: flex-end;
            gap: 12px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            transition: border-color var(--transition-snappy);
        }

        .input-box:focus-within {
            border-color: var(--accent-primary);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 0 1px var(--accent-glow);
        }

        .attach-btn {
            padding: 8px;
            color: var(--text-muted);
            border-radius: var(--radius-sm);
            transition: var(--transition-snappy);
            margin-bottom: 2px;
        }
        .attach-btn:hover { color: var(--text-main); background: var(--bg-elevated); }

        .textarea-container {
            flex: 1;
            position: relative;
        }

        .textarea-container textarea {
            width: 100%;
            background: transparent;
            border: none;
            color: var(--text-main);
            font-size: 1rem;
            resize: none;
            max-height: 150px;
            min-height: 24px;
            padding: 8px 0;
            line-height: 1.5;
        }
        
        .textarea-container textarea::placeholder {
            color: var(--text-muted);
        }

        .send-btn {
            background: var(--accent-primary);
            color: var(--bg-base);
            width: 40px;
            height: 40px;
            border-radius: var(--radius-sm);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 2px;
            transition: var(--transition-snappy);
        }
        .send-btn:hover {
            background: var(--accent-muted);
            transform: scale(0.95);
        }

        .footer-text {
            text-align: center;
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 12px;
        }

        /* --- MODALS (Login & Profile) --- */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity var(--transition-smooth);
        }

        .modal-overlay.active {
            opacity: 1;
            pointer-events: all;
        }

        .modal-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            padding: 40px;
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 400px;
            transform: translateY(20px) scale(0.95);
            transition: all var(--transition-smooth);
            position: relative;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
        }

        .modal-overlay.active .modal-card {
            transform: translateY(0) scale(1);
        }

        .modal-card::before {
            content: '';
            position: absolute;
            top: -1px; left: 20%; right: 20%; height: 1px;
            background: linear-gradient(90deg, transparent, var(--accent-primary), transparent);
            opacity: 0.5;
        }

        .close-modal {
            position: absolute;
            top: 20px; right: 20px;
            color: var(--text-muted);
        }
        .close-modal:hover { color: var(--text-main); }

        /* Login Specifics */
        .modal-title {
            font-family: var(--font-display);
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .modal-subtitle {
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-bottom: 32px;
        }

        .input-group {
            margin-bottom: 20px;
        }
        .input-group label {
            display: block;
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 8px;
            font-weight: 500;
        }
        .input-group input {
            width: 100%;
            background: var(--bg-base);
            border: 1px solid var(--border-subtle);
            padding: 14px 16px;
            border-radius: var(--radius-sm);
            color: var(--text-main);
            transition: border-color 0.2s;
        }
        .input-group input:focus {
            border-color: var(--accent-primary);
        }

        .btn-primary {
            width: 100%;
            background: var(--text-main);
            color: var(--bg-base);
            padding: 14px;
            border-radius: var(--radius-sm);
            font-weight: 600;
            font-size: 1rem;
            margin-top: 10px;
            transition: transform 0.2s;
        }
        .btn-primary:hover {
            transform: scale(0.98);
        }

        /* Profile Specifics */
        .profile-content {
            text-align: center;
        }
        .profile-content .avatar-large {
            width: 80px; height: 80px;
            border-radius: 50%;
            margin: 0 auto 16px;
            background: url('https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop') center/cover;
            border: 2px solid var(--accent-primary);
            padding: 4px;
            background-clip: content-box;
        }
        .profile-stats {
            display: flex;
            justify-content: center;
            gap: 24px;
            margin: 24px 0;
            padding: 16px 0;
            border-top: 1px solid var(--border-subtle);
            border-bottom: 1px solid var(--border-subtle);
        }
        .stat-item {
            display: flex; flex-direction: column;
        }
        .stat-val { font-family: var(--font-display); font-size: 1.2rem; font-weight: 700; color: var(--text-main); }
        .stat-label { font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }

        .btn-secondary {
            background: var(--bg-elevated);
            color: var(--text-main);
            border: 1px solid var(--border-highlight);
            padding: 12px;
            width: 100%;
            border-radius: var(--radius-sm);
            margin-top: 8px;
            display: flex; align-items: center; justify-content: center; gap: 8px;
            font-weight: 500;
        }
        .btn-secondary:hover { background: var(--border-subtle); }
        .btn-danger { color: #ff4545; }

        /* Responsive */
        @media (max-width: 1024px) {
            .chat-container { padding: 100px 10% 140px 10%; }
            .input-wrapper { left: 10%; right: 10%; }
        }
        @media (max-width: 768px) {
            .sidebar { display: none; }
            .chat-container { padding: 80px 5% 140px 5%; }
            .input-wrapper { left: 5%; right: 5%; bottom: 20px; }
        }

    </style>
</head>
<body>

    <div id="app">
        <!-- SIDEBAR -->
        <aside class="sidebar">
            <div class="brand">
                <div class="brand-logo"><i class="ph-bold ph-trend-up"></i></div>
                <div class="brand-name">Equinox</div>
            </div>

            <button class="btn-new-chat" onclick="clearChat()">
                New plan
                <i class="ph-bold ph-plus"></i>
            </button>

            <div class="history-section">
                <div class="history-label">Active Plans</div>
                <button class="history-item active">
                    <i class="ph ph-chart-pie-slice"></i>
                    2024 Budget Optimization
                </button>
                <button class="history-item">
                    <i class="ph ph-bank"></i>
                    High-Yield Savings Options
                </button>
                
                <div class="history-label" style="margin-top: 24px;">Recent Analysis</div>
                <button class="history-item">
                    <i class="ph ph-trend-up"></i>
                    Tech ETF Portfolio Check
                </button>
                <button class="history-item">
                    <i class="ph ph-house"></i>
                    Mortgage Rate Projection
                </button>
                <button class="history-item">
                    <i class="ph ph-shield-check"></i>
                    Emergency Fund Structuring
                </button>
            </div>

            <div class="user-widget" onclick="openModal('profile-modal')">
                <div class="avatar"></div>
                <div class="user-info">
                    <div class="user-name">David Chen</div>
                    <div class="user-plan">Equinox Wealth</div>
                </div>
                <i class="ph ph-gear" style="color: var(--text-muted);"></i>
            </div>
        </aside>

        <!-- MAIN AREA -->
        <main class="main-area">
            <header class="top-bar">
                <div class="model-selector">
                    Equinox-Financial-v2
                    <i class="ph-bold ph-caret-down" style="font-size: 0.8rem;"></i>
                </div>
                <button class="login-btn-top" onclick="openModal('login-modal')">Sign in</button>
            </header>

            <div class="chat-container" id="chat-box">
                <!-- User Message -->
                <div class="message user">
                    <div class="message-avatar"><i class="ph ph-user"></i></div>
                    <div class="message-content">
                        Can you analyze my current spending patterns and suggest a budget framework? I want to save $12,000 this year for a home downpayment while keeping my current salary.
                    </div>
                </div>

                <!-- AI Message with Financial Component -->
                <div class="message ai">
                    <div class="message-avatar"><i class="ph-bold ph-trend-up"></i></div>
                    <div class="message-content">
                        Based on your securely linked accounts, your current monthly net income is $6,200. To reach a $12,000 goal in 12 months, you need to allocate $1,000/month to savings. 
                        <br><br>
                        I recommend adopting a strict <strong>50/30/20 budget model</strong>. Here is your personalized breakdown:
                        
                        <!-- Financial Data Block -->
                        <div class="finance-block">
                            <div class="finance-header">
                                <div class="finance-badge"><i class="ph-bold ph-target"></i> Recommended Plan</div>
                                <span style="font-size: 0.85rem; color: var(--text-muted);"><i class="ph-fill ph-lock-key"></i> Data Synced</span>
                            </div>
                            
                            <div class="finance-body">
                                <div class="finance-total">$6,200<span style="font-size: 1.2rem; color: var(--text-muted);">/mo</span></div>
                                <div class="finance-subtitle">Target Net Income Distribution</div>
                                
                                <!-- Bar 1: Needs -->
                                <div class="budget-row">
                                    <div class="budget-labels">
                                        <span><span style="color: var(--accent-primary); margin-right: 6px;">●</span>Needs (50%)</span>
                                        <span class="budget-val">$3,100</span>
                                    </div>
                                    <div class="bar-container"><div class="bar-fill fill-needs"></div></div>
                                </div>

                                <!-- Bar 2: Wants -->
                                <div class="budget-row">
                                    <div class="budget-labels">
                                        <span><span style="color: #3B82F6; margin-right: 6px;">●</span>Wants (30%)</span>
                                        <span class="budget-val">$1,860</span>
                                    </div>
                                    <div class="bar-container"><div class="bar-fill fill-wants"></div></div>
                                </div>

                                <!-- Bar 3: Savings Goal -->
                                <div class="budget-row">
                                    <div class="budget-labels">
                                        <span><span style="color: #8B5CF6; margin-right: 6px;">●</span>Savings & Debt (20%)</span>
                                        <span class="budget-val" style="color: var(--text-main); font-weight: 600;">$1,240</span>
                                    </div>
                                    <div class="bar-container"><div class="bar-fill fill-savings"></div></div>
                                </div>
                            </div>

                            <div class="finance-footer">
                                <button class="btn-action"><i class="ph ph-arrows-clockwise"></i> Recalculate</button>
                                <button class="btn-action"><i class="ph ph-export"></i> Export to CSV</button>
                                <button class="btn-action" style="margin-left: auto; color: var(--accent-primary); border-color: var(--accent-glow);"><i class="ph ph-check-circle"></i> Apply to Vault</button>
                            </div>
                        </div>
                        <br>
                        This framework exceeds your goal slightly, putting $1,240 away monthly. I recommend routing this directly to your high-yield savings account on payday. Would you like me to automate this transfer or explain specific banking products that offer higher APY?
                    </div>
                </div>
                
                <div id="anchor"></div> <!-- For auto-scrolling -->
            </div>

            <div class="input-wrapper">
                <div class="input-box">
                    <button class="attach-btn" title="Link Account or Upload Document"><i class="ph-bold ph-link" style="font-size: 1.2rem;"></i></button>
                    <div class="textarea-container">
                        <textarea rows="1" placeholder="Ask about investments, budgeting, or banking..." id="chat-input" oninput="this.style.height = '';this.style.height = this.scrollHeight + 'px'"></textarea>
                    </div>
                    <button class="send-btn" onclick="sendMessage()"><i class="ph-bold ph-arrow-up"></i></button>
                </div>
                <div class="footer-text">Equinox provides AI-driven financial guidance, not certified financial or legal advice. Verify critical transactions.</div>
            </div>
        </main>
    </div>

    <!-- MODAL: LOGIN -->
    <div class="modal-overlay" id="login-modal">
        <div class="modal-card">
            <button class="close-modal" onclick="closeModal('login-modal')"><i class="ph-bold ph-x" style="font-size: 1.2rem;"></i></button>
            <div class="brand-logo" style="margin-bottom: 24px;"><i class="ph-bold ph-trend-up"></i></div>
            <h2 class="modal-title">Secure Login</h2>
            <p class="modal-subtitle">Authenticate to access your portfolio and connected bank accounts.</p>
            
            <div class="input-group">
                <label>Email address</label>
                <input type="email" placeholder="name@company.com">
            </div>
            <div class="input-group">
                <label>Password</label>
                <input type="password" placeholder="••••••••">
            </div>
            
            <button class="btn-primary" onclick="closeModal('login-modal')">Authenticate</button>
            
            <p style="text-align: center; margin-top: 24px; font-size: 0.85rem; color: var(--text-muted);">
                Protected by bank-level 256-bit encryption.
            </p>
        </div>
    </div>

    <!-- MODAL: PROFILE -->
    <div class="modal-overlay" id="profile-modal">
        <div class="modal-card profile-content">
            <button class="close-modal" onclick="closeModal('profile-modal')"><i class="ph-bold ph-x" style="font-size: 1.2rem;"></i></button>
            
            <div class="avatar-large"></div>
            <h2 class="modal-title" style="font-size: 1.4rem;">David Chen</h2>
            <p style="color: var(--accent-primary); font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Equinox Wealth Tier</p>
            
            <div class="profile-stats">
                <div class="stat-item">
                    <span class="stat-val">3</span>
                    <span class="stat-label">Linked Banks</span>
                </div>
                <div class="stat-item">
                    <span class="stat-val">$42k</span>
                    <span class="stat-label">Est Net Worth</span>
                </div>
                <div class="stat-item">
                    <span class="stat-val">2</span>
                    <span class="stat-label">Active Goals</span>
                </div>
            </div>
            
            <button class="btn-secondary"><i class="ph ph-plugs-connected"></i> Manage Connections</button>
            <button class="btn-secondary"><i class="ph ph-file-text"></i> Tax Documents</button>
            <button class="btn-secondary btn-danger" onclick="closeModal('profile-modal')"><i class="ph ph-sign-out"></i> Secure Logout</button>
        </div>
    </div>

    <script>
        // Modal Logic
        function openModal(id) {
            document.getElementById(id).classList.add('active');
        }

        function closeModal(id) {
            document.getElementById(id).classList.remove('active');
        }

        // Close modal on outside click
        window.onclick = function(event) {
            if (event.target.classList.contains('modal-overlay')) {
                event.target.classList.remove('active');
            }
        }

        // New Chat Logic
        function clearChat() {
            const chatBox = document.getElementById('chat-box');
            // Keep the anchor, remove messages
            chatBox.innerHTML = '<div id="anchor"></div>';
            
            // Add a welcome state tailored to finance
            const welcomeMsg = document.createElement('div');
            welcomeMsg.style.cssText = "margin: auto; text-align: center; color: var(--text-muted); font-family: var(--font-display); font-size: 1.8rem; font-weight: 600; opacity: 0; animation: fadeIn 1s forwards; max-width: 500px; line-height: 1.4;";
            welcomeMsg.innerHTML = '<i class="ph-bold ph-shield-check" style="color: var(--accent-primary); font-size: 2.5rem; margin-bottom: 16px; display: block;"></i>How can I assist with your financial goals today?';
            chatBox.insertBefore(welcomeMsg, document.getElementById('anchor'));

            // Remove active state from history
            document.querySelectorAll('.history-item').forEach(item => item.classList.remove('active'));
        }

        // Send Message Logic (UI Mockup)
        function sendMessage() {
            const input = document.getElementById('chat-input');
            const text = input.value.trim();
            if(!text) return;

            const chatBox = document.getElementById('chat-box');
            const anchor = document.getElementById('anchor');

            // If welcome message exists, remove it
            if(chatBox.children.length === 2 && chatBox.children[0].tagName === 'DIV' && !chatBox.children[0].classList.contains('message')) {
                chatBox.children[0].remove();
            }

            // Create User Message
            const userHtml = `
                <div class="message user">
                    <div class="message-avatar"><i class="ph ph-user"></i></div>
                    <div class="message-content">${text}</div>
                </div>
            `;
            anchor.insertAdjacentHTML('beforebegin', userHtml);

            // Reset Input
            input.value = '';
            input.style.height = '24px'; // reset height

            // Scroll to bottom
            chatBox.scrollTop = chatBox.scrollHeight;

            // Simulate AI Loading/Typing
            setTimeout(() => {
                const aiHtml = `
                    <div class="message ai">
                        <div class="message-avatar"><i class="ph-bold ph-trend-up"></i></div>
                        <div class="message-content">
                            <span style="display:inline-block; width: 8px; height: 8px; background: var(--accent-primary); border-radius: 50%; animation: pulse 1s infinite alternate;"></span>
                        </div>
                    </div>
                `;
                anchor.insertAdjacentHTML('beforebegin', aiHtml);
                chatBox.scrollTop = chatBox.scrollHeight;
                
                // Simulate AI Response
                setTimeout(() => {
                    const lastMsg = anchor.previousElementSibling;
                    lastMsg.querySelector('.message-content').innerHTML = `I understand. I am currently operating in prototype mode, so I cannot execute live financial transactions or pull real-time market data. However, I have registered your inquiry regarding "${text.substring(0, 20)}..." and can assist with theoretical modeling if you provide hypothetical numbers.`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                }, 1200);

            }, 400);
        }

        // Handle Enter key to send
        document.getElementById('chat-input').addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    </script>
</body>
</html>