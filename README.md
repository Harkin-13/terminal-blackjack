# Terminal Blackjack 🃏

A clean, object-oriented Blackjack game written in Python.  
Perfect for the command line; designed as a portfolio piece to demonstrate class design, game-loop control flow, and basic state management.

## Features
- **Card / Deck / Player / Dealer** classes in separate modules  
- Full Blackjack rules with Ace-value handling (1 or 11)  
- Instant win/tie detection for natural 21s  
- Auto-dealer logic (hit ≤ 16, stand ≥ 17)  
- Clear terminal UI with helper function `show_hand()`  
- Replay loop

## How to Run
```bash
python main.py
(Requires Python 3.10+; no external libraries)
