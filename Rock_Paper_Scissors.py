import random
import cv2
from keras.models import load_model
import numpy as np
import time
import warnings
warnings.filterwarnings('ignore')
from keras import backend as K
K.clear_session()

# Timer for the game
TIMER = int(5)
# Read and display each frame
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    cv2.imshow('Rock_paper_scissors', frame)

    prev = time.time()

    while TIMER >= 0:
        ret, frame = cap.read()

        # Display countdown on each frame
        # specify the font and draw the
        # countdown using puttext
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(TIMER),
                    (200, 250), font,
                    7, (255, 0, 0),
                    4, cv2.LINE_AA)

        cv2.imshow('Rock_paper_scissors', frame)
        cv2.waitKey(125)

        # current time
        cur = time.time()

        # Update and keep track of Countdown
        # if time elapsed is one second
        # than decrease the counter
        if cur-prev >= 1:
            prev = cur
            TIMER = TIMER-1 



    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (200, 250)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2


    ret, frame = cap.read()
    cv2.putText(frame, 'Game Starting!', org, font, 
           fontScale, color, thickness, cv2.LINE_AA)

    # Display the clicked frame for 2
    # sec.You can increase time in
    # waitKey also
    cv2.imshow('Rock_paper_scissors', frame)

    # time for which image displayed
    cv2.waitKey(2500)
            

    break
    
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
 

def webcam_input():
    cap = cv2.VideoCapture(0)
    model = load_model('keras_model.h5', compile=False)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    while True:

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('Rock_paper_scissors', frame)


        if prediction[0][0] > 0.5:
            pred = 'Rock'
        elif prediction[0][1] > 0.5:
            pred = 'Paper'
        elif prediction[0][2] > 0.5:
            pred = 'Scissor'
        else:
            pred = 'Nothing'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()    

    return pred

    

  
 
def rock_paper_scissors():
    
    player_wins = 0
    computer_wins = 0

    # t = input("Enter time in seconds: ")
    # countdown_timer(t)
    
    while player_wins < 3 and computer_wins < 3:

        options = ['Rock', 'Paper', 'Scissor']

        computer_choice = random.choice(options).lower()
        computer_choice = computer_choice.lower()

        print("Enter your choice: ")
        your_choice = webcam_input()
        your_choice = your_choice.lower()


        while your_choice == computer_choice:
            print("Tie, play again:")
            computer_choice = random.choice(options).lower()
            your_choice = webcam_input()
            your_choice = your_choice.lower()

        while your_choice == 'Nothing':
            print("Invalid input, try again:")
            your_choice = webcam_input()
            your_choice = your_choice.lower()

        if your_choice == 'scissor' and computer_choice == 'paper':
            print('You win!')
            print("Computer chose: {}".format(computer_choice))
            print("You chose: {}".format(your_choice))

            player_wins += 1

        elif your_choice == 'scissor' and computer_choice == 'rock':
            print('You lose!')
            print("Computer chose: {}".format(computer_choice))
            print("You chose: {}".format(your_choice))

            computer_wins += 1

        elif your_choice == 'paper' and computer_choice == 'rock':
            print('You win!')
            print("Computer chose: {}".format(computer_choice))
            print("You chose: {}".format(your_choice))

            player_wins += 1

        elif your_choice == 'paper' and computer_choice == 'scissor':
            print('You lose!')
            print("Computer chose: {}".format(computer_choice))
            print("You chose: {}".format(your_choice))

            computer_wins += 1

        elif your_choice == 'rock' and computer_choice == 'scissor':
            print('You win!')
            print("Computer chose: {}".format(computer_choice))
            print("You chose: {}".format(your_choice))

            player_wins += 1

        elif your_choice == 'rock' and computer_choice == 'paper':
            print('You lose!')
            print("Computer chose: {}".format(computer_choice))
            print("You chose: {}".format(your_choice))

            computer_wins += 1
        else:
            pass
    
    if player_wins == 3:
        print('You reached 3 wins first, congratulations! The computer only won {} games'.format(computer_wins))
    
    else:
        print('You lost overall and won only {} out of 3 games!'.format(player_wins))
    
  
 
        
rock_paper_scissors()
        
