/* 
    Display the local postgres data in a chart using Chart.js.
    1. Gather the data
    2. Call the Chart constructor. Settings are organized in JSON.
*/

/* 
    1. Gather the data:
    Referencing values from the Context Dictionary from the template for use in JavaScript.
*/
   const Q1_A = JSON.parse(document.getElementById('Q1_A').textContent);
   const Q1_B = JSON.parse(document.getElementById('Q1_B').textContent);
   const Q1_C = JSON.parse(document.getElementById('Q1_C').textContent);
   const Q1_D = JSON.parse(document.getElementById('Q1_D').textContent);

/* 
Chart.js for the RestAPI Consumer Chart 

Description:
Chart objects are created with the Chart constructor. Ex: 'new Chart(context, config)'
    context = the call to getElementById, referencing the <canvas> tag.
    config = Specifies the chart's: type, data, and options.

    In the end, we will make a simple call:
    const chart2 = new Chart( context2, config2 );

    The structure really like this:
    Charts (
        context,
        config:
            type
            data: Setup    The values for the 'data' key are refereed to as 'Setup' in the charts.js doc.
            options        So, it's best to store those values in variable named 'Setup'. 
            )

    Now we define these configs as JSON, stored as const objects, before making the call to the Charts constructor.
*/

//The context for chart 1
const context = document.getElementById('chart1').getContext('2d');

// This setUp block will be assigned to the 'data' key of the 'config' block below.
const setup = {
    labels: ['not legitimate', 'legitimate earthly', 'legitimate earthly few extraterrestrial', 'legitimate extraterrestrial'],
    datasets: [{
        label: '# of Votes',
        data: [Q1_A, Q1_B, Q1_C, Q1_D],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(255, 206, 86, 0.2)'
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(54, 162, 235, 1)'
        ],
        borderWidth: 1
    }]
}
const config = {
    type: 'pie',
    data: setup,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
}

//Nice, simple constructor of a new Chart.js chart for our RestAPI consuming Chart.
const chart1 = new Chart( context, config );


/* 
Chart.js 101 

Description:
Chart objects are created with the Chart constructor. Ex: 'new Chart(context, config2)'
    context = The famous JS function getElementById references the <canvas>'s ID tag.
    config = Comprises of 3 distinct meta data objects: 1) type, 2) data, and 3) options.
        The 'data' object is called 'Setup' in the Charts.js online documentation

    In the end, we will make a simple call:
    const chart2 = new Chart( context, config );
        where config is a JSON object

    The structure really like this:
    Charts (
        context,
        config:
            type
            data: Setup    it's best to compartmentalize the values for the data key into a 
            options        variable called Setup to stay on-page with the chart.js documentation. 
            )

    Now we define these configs as JSON stored as const objects before making the call to the Charts constructor.
*/


/* 
    1. Gather the data:
    Referencing values from the Context Dictionary from the template for use in JavaScript.

    Or 

    Make the GET Request from here.
*/


/* Rest API Consumption 101  
 *
 * 1. Define async function
 * 2. Call that async function
 */

let url_lansing = 'https://api.openweathermap.org/data/2.5/weather?q=lansing&appid=a8efcfe69258b521961181dac55090ca'
let tempK = 0
let tempChicago = 0

console.log('Test')

async function getapi(url_lansing) {
    
    // Storing response
    const response = await fetch(url_lansing);
    
    // Storing data in form of JSON
    var data = await response.json();

    tempK = data.main.temp
    tempChicago = ((tempK-273.15)*1.8)+32
    tempChicago = Math.round(tempChicago)
    console.log(tempChicago)
    console.log('Test')

    if (response) {
        // execute function
    }
}

getapi(url_lansing);

//The context for RestAPI Consumer Chart
const context2 = document.getElementById('myChart2');

//The config for RestAPI Consumer Chart
const config2 = {
    type: 'bar',
    data: { /* aka the setup */
        labels: ['Chicago', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [tempChicago, 0, 0, 0, 0, 0],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

// The data

//Nice and simple chart constructor statement for the RestAPI Consumer Chart. 
const chart2 = new Chart(context2, config2);
