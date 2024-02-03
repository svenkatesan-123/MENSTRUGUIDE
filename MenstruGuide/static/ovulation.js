let res= document.getElementById("result");
let ov= document.getElementById("ovtracker");
function resdis(){
    res.style.display="flex";
    ov.style.display="none";
}


function calculate(event) {
    event.preventDefault();
  
    // Get the input values
    const lastPeriodDate = new Date(document.getElementById("last-period-date").value);
    const cycleLength = Number(document.getElementById("cycle-length").value);
  
    // Calculate the ovulation date
    const ovulationDate = new Date(lastPeriodDate.getTime() + (cycleLength - 14) * 24 * 60 * 60 * 1000);
  
    // Calculate the fertility period
    const fertilityStartDate = new Date(ovulationDate.getTime() - 5 * 24 * 60 * 60 * 1000);
    const fertilityEndDate = new Date(ovulationDate.getTime());
  
    // Display the results
    resdis();
    
    document.getElementById("ovulation-date").textContent = formatDate(ovulationDate);
    document.getElementById("fertility-period").textContent = formatDate(fertilityStartDate) + " - " + formatDate(fertilityEndDate);
  
    // Generate the calendar
    const calendar = document.getElementById("calendar");
   
    calendar.innerHTML = "";
  
    // Add the days of the week
    const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
   
    for (let i = 0; i < daysOfWeek.length; i++) {
      const day = document.createElement("div");
      day.classList.add("day");
      day.style.background="yellow";
      
      day.textContent = daysOfWeek[i];
      calendar.appendChild(day);
    }
  
    // Calculate the start date of the calendar
    const startDate = new Date(lastPeriodDate.getTime() - 14 * 24 * 60 * 60 * 1000);
    startDate.setDate(startDate.getDate() - startDate.getDay());
  
    // Add the days to the calendar
    const endDate = new Date(lastPeriodDate.getTime() + (cycleLength - 1) * 24 * 60 * 60 * 1000);
    let currentDate = new Date(startDate);


    let k=0;
    while (currentDate <= endDate) {
      const day = document.createElement("div");
     
      day.classList.add("day");
      day.textContent = currentDate.getDate();
     
      if(currentDate.getDate()==(lastPeriodDate.getDate())){
        day.style.background="lightgreen";
      }

     
      if (currentDate.getTime() === ovulationDate.getTime()) {
        day.classList.add("ovulation");
      } else if (currentDate >= fertilityStartDate && currentDate <= fertilityEndDate) {
        day.classList.add("fertility");
      }
  
      if (currentDate.getTime() === new Date().setHours(0, 0, 0, 0)) {
        day.classList.add("today");
      }
  
      calendar.appendChild(day);
      currentDate.setDate(currentDate.getDate() + 1);
    }
  }
  
  function formatDate(date) {
    const options = { year: "numeric", month: "long", day: "numeric" };
    return date.toLocaleDateString("en-US", options);
  }
  
  document.querySelector("form").addEventListener("submit", calculate);
  

