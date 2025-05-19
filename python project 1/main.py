import random
import tkinter as tk

def create_game():
    window = tk.Tk()
    window.title("Snake-Water-Gun Game")
    window.geometry("400x400")
    window.configure(bg='lightblue')
    
    player_score = 0
    computer_score = 0
    
    # Display labels
    tk.Label(window, text="Snake-Water-Gun Game", font=('Arial', 20), bg='lightblue').pack(pady=20)
    
    result_label = tk.Label(window, text="Choose your move!", font=('Arial', 12), bg='lightblue')
    result_label.pack(pady=10)
    
    score_label = tk.Label(window, text="Score: 0 - 0", font=('Arial', 12), bg='lightblue')
    score_label.pack(pady=10)
    
    def play_game(player_choice):
        nonlocal player_score, computer_score
        
        choices = {
            'snake': '🐍',
            'water': '💧',
            'gun': '🔫'
        }
        
        computer_choice = random.choice(list(choices.keys()))
        
        # Determine winner
        if player_choice == computer_choice:
            result = "Draw!"
            color = 'black'
        elif ((player_choice == 'snake' and computer_choice == 'water') or 
              (player_choice == 'water' and computer_choice == 'gun') or 
              (player_choice == 'gun' and computer_choice == 'snake')):
            result = "You Win!"
            color = 'green'
            player_score += 1
        else:
            result = "Computer Wins!"
            color = 'red'
            computer_score += 1
            
        # Update labels
        result_label.config(text=f"You: {choices[player_choice]} vs Computer: {choices[computer_choice]}\n{result}", fg=color)
        score_label.config(text=f"Score: {player_score} - {computer_score}")
    
    # Create buttons
    buttons_frame = tk.Frame(window, bg='lightblue')
    buttons_frame.pack(pady=20)
    
    tk.Button(buttons_frame, text="🐍 Snake", command=lambda: play_game('snake')).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="💧 Water", command=lambda: play_game('water')).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="🔫 Gun", command=lambda: play_game('gun')).pack(side=tk.LEFT, padx=5)
    
    tk.Button(window, text="Quit", command=window.destroy).pack(pady=20)
    
    window.mainloop()

if __name__ == "__main__":
    create_game()
