function calculateDueDate() {
    const lastPeriod = new Date(document.getElementById("last-period").value);
    const cycleLength = document.getElementById("cycle-length").value;
    
    // Validate cycle length
    if (cycleLength < 21 || cycleLength > 35) {
      alert("Please enter a valid average cycle length between 21 and 35 days.");
      return;
    }
    var resres=document.getElementById("res-res");
    resres.style.width="100%";
    var resres1=document.getElementById("res-res1");
    resres1.style.width="100%";
    var resres2=document.getElementById("res-res2");
    resres2.style.width="100%";
    // Calculate due date
    const dueDate = new Date(lastPeriod);
    dueDate.setDate(dueDate.getDate() + 280); // 280 days in a pregnancy
    
    // Calculate gestational age
    const today = new Date();
    const gestationalAgeInDays = Math.floor((today - lastPeriod) / (1000 * 60 * 60 * 24));
    const gestationalAgeInWeeks = Math.floor(gestationalAgeInDays / 7);
    const gestationalAgeInDaysRemainder = gestationalAgeInDays % 7;
    const gestationalAge = `${gestationalAgeInWeeks} weeks and ${gestationalAgeInDaysRemainder} days`;
    
    // Calculate trimester timeline
    const trimesterOneEnd = new Date(lastPeriod);
    trimesterOneEnd.setDate(trimesterOneEnd.getDate() + 12 * 7); // 12 weeks in first trimester
    const trimesterTwoEnd = new Date(lastPeriod);
    trimesterTwoEnd.setDate(trimesterTwoEnd.getDate() + 24 * 7); // 24 weeks in second trimester
    
    // Date restrictions
    const maxDate = new Date();
    maxDate.setMonth(maxDate.getMonth() - 10); // Can't be more than 10 months old
    maxDate.setHours(0,0,0,0); // Set time to midnight
    
    if (lastPeriod < maxDate) {
      alert("Please select a valid date range. The last period date cannot be more than 10 months from today.");
      return;
    }
    if(lastPeriod>today){
      alert("Please select a valid date range.");
      return;
    }
    
    // Show results
    document.getElementById("due-date").textContent = dueDate.toDateString();
    document.getElementById("gestational-age").textContent = gestationalAge;
    document.getElementById("trimester-timeline").textContent = `First Trimester: ${lastPeriod.toDateString()} - ${trimesterOneEnd.toDateString()} | Second Trimester: ${trimesterOneEnd.toDateString()} - ${trimesterTwoEnd.toDateString()} | Third Trimester: ${trimesterTwoEnd.toDateString()} - ${dueDate.toDateString()}`;
    document.querySelector(".result").style.display = "block";
  }
  