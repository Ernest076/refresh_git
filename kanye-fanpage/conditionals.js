let age = 16;
if (age < 18) {
    console.log("You are a minor.");
} else {
    console.log("You are an adult.");
}
let age2 = 18;
if (age >= 18) {
    console.log("You are allowed to drive.");
} else {
    console.log("You are not allowed to drive.");
}
let score = 77;
if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else if (score >= 60) {
    console.log("Grade: D");
}
let temperature = 23;
if (temperature > 23) {
    console.log("It's a hot day.");
}
if (temperature < 15) {
    console.log("It's a cold day.");
} else {
    console.log("It's a pleasant day.");
}
let isLoggedIn = true;
let isNotLoggedIn = false;

if (isLoggedIn) {
    console.log("Welcome back!");
}else if (isNotLoggedIn){
    console.log("Please log in to continue.");
}else {
    console.log("Unknown user status.");
}
let isAdmin = true;
let isEditor = false;
if (isAdmin || isEditor) {
    console.log("You have access to edit content.");
}else if (!isAdmin && !isEditor) {
    console.log("You do not have access to edit content.");
}
let isHoliday = false;
if (!isHoliday) {
    console.log("It's a working day."); 
} else {
    console.log("It's a holiday! Enjoy your day off.");
}
let batteryLevel = 75;
if (batteryLevel <= 55) {
    console.log("Battery is low. Please charge your device.");
}
else if (batteryLevel >= 55) {
    console.log("Battery level is sufficient.");
}else if (batteryLevel > 55) {
    console.log("Perfect battery status.");
}