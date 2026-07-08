from psychopy import visual, core, event, gui
import random
import pandas as pd

# 1. Participant Info
exp_info = {'Participant': '001', 'Session': '1'}
dlg = gui.DlgFromDict(dictionary=exp_info, title="Reaction Time Task")
if not dlg.OK:
    core.quit()

# 2. Setup Window and Global Clock
win = visual.Window([1200, 800], monitor="testMonitor", units="deg", color="black")
global_clock = core.Clock() # Starts at 0.0 now
exp_data = []

# Define Stimuli
stim_info = [
    {'image': 'up_img.png', 'color_label': 'red', 'correct_key': 'up'},
    {'image': 'right_img.png', 'color_label': 'black', 'correct_key': 'right'},
    {'image': 'left_img.png', 'color_label': 'blue', 'correct_key': 'left'}
]

# 3. Instructions
instr_text = (
    "RED ball = UP | BLACK ball = RIGHT | BLUE ball = LEFT\n\n"
    "Respond as fast as possible.\n"
    "Press SPACE to exit early.\n\n"
    "Press any key to BEGIN."
)
visual.TextStim(win, text=instr_text, color='white', height=0.7).draw()
win.flip()
event.waitKeys()

# 4. Main Game Loop (30 Trials)
for t_idx in range(30):
    trial = random.choice(stim_info).copy()
    
    # Logic: Probability of failure increases as trials go on
    # Starts at 0% failure, ends at ~60% failure
    failure_chance = (t_idx / 30) * 0.6
    buttons_worked = random.random() > failure_chance
    
    # Set up Stimulus
    stim = visual.ImageStim(win, image=trial['image'])
    
    # RANDOM SPEED: Inter-trial interval (0.4s to 1.2s)
    core.wait(random.uniform(0.4, 1.2))
    
    # Reset Trial Variables
    press_count = 0
    first_key = None
    first_rt = None
    # Timestamp of when this specific image appeared relative to game start
    appearance_timestamp = global_clock.getTime()
    
    event.clearEvents()
    stim.draw()
    win.flip()
    trial_clock = core.Clock()
    
    # 5. Response Handling
    continue_trial = True
    while continue_trial:
        # Check for exit key
        all_keys = event.getKeys(keyList=['up', 'left', 'right', 'space'], timeStamped=trial_clock)
        
        for key, timestamp in all_keys:
            if key == 'space': # Emergency Exit
                win.close()
                df = pd.DataFrame(exp_data)
                df.to_csv(f"PART_{exp_info['Participant']}_INTERRUPTED.csv", index=False)
                core.quit()
                
            press_count += 1
            if first_key is None:
                first_key = key
                first_rt = timestamp
            
            # If buttons WORK: Close image immediately on first press
            if buttons_worked:
                continue_trial = False
                break
        
        # If buttons DON'T WORK: Force them to wait 4 seconds
        if not buttons_worked and trial_clock.getTime() > 4.0:
            continue_trial = False

    # 6. Scoring
    accuracy = "Correct" if first_key == trial['correct_key'] else "Wrong"
    if first_key is None: accuracy = "No Response"

    # 7. Data Logging
    exp_data.append({
        'Participant': exp_info['Participant'],
        'Trial': t_idx + 1,
        'Color': trial['color_label'],
        'Game_Timestamp': appearance_timestamp, # When image appeared
        'Result': accuracy,
        'Buttons_Worked': "Yes" if buttons_worked else "No",
        'Reaction_Time': first_rt,
        'Total_Presses': press_count
    })
    
    # Brief blank screen between trials
    win.flip()
    core.wait(0.2)

# 8. Final Save
win.close()
df = pd.DataFrame(exp_data)
file_name = f"Part_{exp_info['Participant']}_Session_{exp_info['Session']}.csv"
df.to_csv(file_name, index=False)
print(f"Data saved to {file_name}")
core.quit()