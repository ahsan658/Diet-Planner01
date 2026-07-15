import sys
!{sys.executable} -m pip install streamlit
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BMI & Diet Planner",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 BMI & Diet Planner")
st.write("Calculate your BMI and get a personalized diet plan.")

st.divider()

# User Inputs
name = st.text_input("Enter Your Name")

age = st.number_input(
    "Age",
    min_value=5,
    max_value=100,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

height = st.number_input(
    "Height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=10.0,
    max_value=300.0,
    value=70.0
)

if st.button("Calculate BMI"):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    st.subheader(f"Hello {name}!")

    st.metric("Your BMI", f"{bmi:.2f}")

    # Healthy weight range
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)

    st.info(
        f"Healthy Weight Range: **{min_weight:.1f} kg - {max_weight:.1f} kg**"
    )

    # Water recommendation
    water = weight * 35 / 1000
    st.success(f"💧 Recommended Water Intake: {water:.1f} Liters/day")

    st.divider()

    # BMI Categories

    if bmi < 18.5:

        st.warning("BMI Category: Underweight")

        st.subheader("🍽 Diet Plan")

        st.markdown("""
### Breakfast
- Milk
- Eggs
- Peanut Butter
- Whole Wheat Bread
- Banana

### Lunch
- Chicken
- Rice
- Vegetables
- Yogurt

### Evening Snack
- Dry Fruits
- Smoothie

### Dinner
- Fish or Chicken
- Brown Rice
- Salad

### Recommendations
- Increase calorie intake.
- Eat protein-rich foods.
- Strength training 3-4 days/week.
- Sleep 7-8 hours.
""")

    elif bmi < 25:

        st.success("BMI Category: Normal Weight")

        st.subheader("🥗 Diet Plan")

        st.markdown("""
### Breakfast
- Oatmeal
- Fruits
- Boiled Eggs

### Lunch
- Grilled Chicken
- Brown Rice
- Vegetables

### Evening Snack
- Nuts
- Green Tea

### Dinner
- Fish
- Salad
- Soup

### Recommendations
- Maintain balanced diet.
- Exercise 30 minutes daily.
- Drink enough water.
""")

    elif bmi < 30:

        st.warning("BMI Category: Overweight")

        st.subheader("🥬 Diet Plan")

        st.markdown("""
### Breakfast
- Oats
- Green Tea
- Apple

### Lunch
- Grilled Chicken
- Mixed Vegetables
- Salad

### Evening Snack
- Almonds

### Dinner
- Vegetable Soup
- Grilled Fish

### Recommendations
- Reduce sugar.
- Avoid soft drinks.
- Walk 45 minutes daily.
- Eat more vegetables.
""")

    else:

        st.error("BMI Category: Obese")

        st.subheader("🥦 Diet Plan")

        st.markdown("""
### Breakfast
- Boiled Eggs
- Oats
- Green Tea

### Lunch
- Grilled Chicken
- Steamed Vegetables

### Evening Snack
- Fruits

### Dinner
- Vegetable Soup
- Salad

### Recommendations
- Avoid junk food.
- Avoid sugary drinks.
- Exercise 60 minutes daily.
- Consult a doctor or dietitian.
""")

    st.divider()

    st.caption("⚠️ This diet plan is for educational purposes only and is not a substitute for professional medical advice.")
