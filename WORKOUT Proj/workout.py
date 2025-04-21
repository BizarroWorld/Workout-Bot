from flask import Flask, request, jsonify, session, render_template

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template("index.html")
    initial_message = """
   
    <h1>Workout AI Chatbot:</h1>
    <p>Please select your equipment and muscle group:</p>
    <ul>
        <li>1. Dumbbells</li>
        <li>2. Barbells</li>
        <li>3. Pull-up-bar</li>
        <li>4. Bench</li>
        <li>5. Cable</li>
        <li>6. Kettlebells</li>
    </ul>
    <p>And muscle group:</p>
    <ul>
        <li>A: Abs</li>
        <li>B: Back</li>
        <li>C: Biceps</li>
        <li>D: Chest</li>
        <li>E: Hamstrings</li>
        <li>F: Quadriceps</li>
        <li>G: Shoulders</li>
        <li>H: Triceps</li>
    </ul>
    <form action="/chat" method="post">
        <label for="message">Type your choice (e.g., 1A):</label>
        <input type="text" id="message" name="message">
        <input type="submit" value="Send">
    </form>
    """
    return initial_message

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = chatbot_response(user_message)
    return jsonify({"response": response})

def chatbot_response(message):
    equipment_options = {
        '1': 'Dumbbells',
        '2': 'Barbells',
        '3': 'Pull-up-bar',
        '4': 'Bench',
        '5': 'Cable',
        '6': 'Kettlebells'
    }
    muscle_group_options = {
        'A': 'Abs',
        'B': 'Back',
        'C': 'Biceps',
        'D': 'Chest',
        'E': 'Hamstrings',
        'F': 'Quadriceps',
        'G': 'Shoulders',
        'H': 'Triceps'
    }

    if len(message) == 2 and message[0] in equipment_options and message[1].upper() in muscle_group_options:
        equipment = equipment_options[message[0]]
        muscle_group = muscle_group_options[message[1].upper()]
        return get_workout(equipment, muscle_group)
    else:
        return "Please enter a valid choice (e.g., 1A for Dumbbells and Abs)."

def get_workout(equipment, muscle_group):
    workouts = {
        ('Dumbbells', 'Abs'): "Dumbbell Russian Twists, Dumbbell Sit-ups: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Back'): "Dumbbell Rows, Dumbbell Deadlifts: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Biceps'): "Dumbbell Curls, Hammer Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Chest'): "Dumbbell Bench Press, Dumbbell Flyes: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Hamstrings'): "Dumbbell Romanian Deadlifts, Dumbbell Leg Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Quadriceps'): "Dumbbell Squats, Dumbbell Lunges: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Shoulders'): "Dumbbell Shoulder Press, Dumbbell Lateral Raises: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Dumbbells', 'Triceps'): "Dumbbell Tricep Extensions, Dumbbell Kickbacks: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Abs'): "Barbell Rollouts, Barbell Russian Twists: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Back'): "Barbell Rows, Barbell Deadlifts: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Biceps'): "Barbell Curls, Reverse Barbell Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Chest'): "Barbell Bench Press, Barbell Incline Press: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Hamstrings'): "Barbell Romanian Deadlifts, Barbell Leg Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Quadriceps'): "Barbell Squats, Barbell Lunges: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Shoulders'): "Barbell Shoulder Press, Barbell Upright Rows: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Barbells', 'Triceps'): "Barbell Skull Crushers, Close Grip Barbell Press: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Abs'): "Hanging Leg Raises, Toes to Bar: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Back'): "Pull-ups, Chin-ups: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Biceps'): "Chin-ups, Hanging Bicep Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Chest'): "Pull-up Bar Push-ups, Hanging Push-ups: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Hamstrings'): "Hanging Leg Curls, Hanging Single Leg Deadlifts: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Quadriceps'): "Hanging Squats, Hanging Lunges: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Shoulders'): "Hanging Shoulder Press, Hanging Lateral Raises: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Pull-up-bar', 'Triceps'): "Hanging Tricep Extensions, Hanging Dips: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Abs'): "Bench V-ups, Bench Leg Raises: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Back'): "Bench Rows, Bench Pullovers: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Biceps'): "Bench Curls, Incline Bench Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Chest'): "Bench Press, Incline Bench Press: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Hamstrings'): "Bench Leg Curls, Bench Hip Thrusts: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Quadriceps'): "Bench Squats, Bench Step-ups: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Shoulders'): "Bench Shoulder Press, Bench Upright Rows: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Bench', 'Triceps'): "Bench Dips, Bench Tricep Extensions: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Abs'): "Cable Crunches, Cable Woodchoppers: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Back'): "Cable Rows, Cable Lat Pulldowns: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Biceps'): "Cable Curls, Cable Hammer Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Chest'): "Cable Chest Press, Cable Flyes: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Hamstrings'): "Cable Leg Curls, Cable Romanian Deadlifts: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Quadriceps'): "Cable Squats, Cable Lunges: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Shoulders'): "Cable Shoulder Press, Cable Lateral Raises: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Cable', 'Triceps'): "Cable Tricep Pushdowns, Cable Tricep Extensions: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Abs'): "Kettlebell Russian Twists, Kettlebell Sit-ups: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Back'): "Kettlebell Swings, Kettlebell Rows: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Biceps'): "Kettlebell Curls, Kettlebell Hammer Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Chest'): "Kettlebell Floor Press, Kettlebell Flyes: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Hamstrings'): "Kettlebell Deadlifts, Kettlebell Leg Curls: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Quadriceps'): "Kettlebell Squats, Kettlebell Lunges: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Shoulders'): "Kettlebell Shoulder Press, Kettlebell Lateral Raises: Sets: 3, Reps: 12, Rest Time: 90 seconds",
        ('Kettlebells', 'Triceps'): "Kettlebell Tricep Extensions, Kettlebell Kickbacks: Sets: 3, Reps: 12, Rest Time: 90 seconds"
    }

    workout = workouts.get((equipment, muscle_group), "Workout not found.")
    return f"Here is a workout for your {muscle_group} using {equipment}: {workout}"

if __name__ == '__main__':
    app.run(debug=True)
