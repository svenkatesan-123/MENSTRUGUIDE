const form = document.getElementById("form");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const lastPeriodDate = new Date(document.getElementById("last-period-date").value);
    const cycleLength = Number(document.getElementById("cycle-length").value);
    const periodLength = Number(document.getElementById("period-length").value);

    // Check if the last period date is within the last 3 months
    const today = new Date();
    const threeMonthsAgo = new Date(today.getFullYear(), today.getMonth() - 3, today.getDate());
    const threeMonthsFromNow = new Date(today.getFullYear(), today.getMonth() + 3, today.getDate());

    if (lastPeriodDate < threeMonthsAgo) {
        resultDiv.innerHTML = `<div class="error">Your last period date seems to be abnormal, kindly consult a doctor.</div>`;
        return;
    }
    if (lastPeriodDate > threeMonthsFromNow) {
        resultDiv.innerHTML = `<div class="error">Your last period date seems to be abnormal, Please input a valid date.</div>`;
        return;
    }

    // Check if period length is not greater than 10
    if (periodLength > 10) {
        resultDiv.innerHTML = `<div class="error">Your period length seems to be abnormal, kindly consult a doctor.</div>`;
        return;
    }

    if(cycleLength<21 || cycleLength>35){
        resultDiv.innerHTML = `<div class="error">Your menstural cycle seems to be abnormal, kindly consult a doctor.</div>`;
        return;
    }

    // Calculate the next period date
    const nextPeriodDate = new Date(lastPeriodDate.getTime() + (cycleLength * 24 * 60 * 60 * 1000));

    // Calculate the period range
    const periodStartDate = nextPeriodDate;
    const periodEndDate = new Date(periodStartDate.getTime() + ((periodLength - 1) * 24 * 60 * 60 * 1000));

    // Display the result
    const formattedNextPeriodDate = formatDate(nextPeriodDate);
    const formattedPeriodStartDate = formatDate(periodStartDate);
    const formattedPeriodEndDate = formatDate(periodEndDate);
    resultDiv.innerHTML = `<div class="result">Your expected period range is from ${formattedPeriodStartDate} to ${formattedPeriodEndDate}.</div>`;
});

function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString(undefined, options);
}
