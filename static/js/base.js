$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

/* Safely Include Data for JavaScript in a Template */
const Q1_A = JSON.parse(document.getElementById('Q1_A').textContent);
const Q1_B = JSON.parse(document.getElementById('Q1_B').textContent);
const Q1_C = JSON.parse(document.getElementById('Q1_C').textContent);
const Q1_D = JSON.parse(document.getElementById('Q1_D').textContent);

const Q2_A = JSON.parse(document.getElementById('Q2_A').textContent);
const Q2_B = JSON.parse(document.getElementById('Q2_B').textContent);

const Q3_A = JSON.parse(document.getElementById('Q3_A').textContent);
const Q3_B = JSON.parse(document.getElementById('Q3_B').textContent);
const Q3_C = JSON.parse(document.getElementById('Q3_C').textContent);
const Q3_D = JSON.parse(document.getElementById('Q3_D').textContent);

const Q4_A = JSON.parse(document.getElementById('Q4_A').textContent);
const Q4_B = JSON.parse(document.getElementById('Q4_B').textContent);
const Q4_C = JSON.parse(document.getElementById('Q4_C').textContent);
const Q4_D = JSON.parse(document.getElementById('Q4_D').textContent);

const Q5_A = JSON.parse(document.getElementById('Q5_A').textContent);
const Q5_B = JSON.parse(document.getElementById('Q5_B').textContent);
const Q5_C = JSON.parse(document.getElementById('Q5_C').textContent);

/* Chart.js | Chart for Question 1 */
/* It appears the variable name of myChart, the second const, doesnt matter. It must only not
match any further charts in the namespace */
const chart1 = document.getElementById('question1').getContext('2d');
const myChart = new Chart(chart1, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green'],
        datasets: [{
            label: '# of Votes',
            data: [Q1_A, Q1_B, Q1_C, Q1_D],
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
});

/* Chart.js | Chart for Question 2 */
const chart2 = document.getElementById('question2').getContext('2d');
const myChart2 = new Chart(chart2, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [Q2_A, Q2_B],
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
});

/* Chart.js | Chart for Question 3 */
const chart3 = document.getElementById('question3').getContext('2d');
const myChart3 = new Chart(chart3, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green'],
        datasets: [{
            label: '# of Votes',
            data: [Q3_A, Q3_B, Q3_C, Q3_D],
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
});


/* Chart.js | Chart for Question 4 */
const chart4 = document.getElementById('question4').getContext('2d');
const myChart4 = new Chart(chart4, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green'],
        datasets: [{
            label: '# of Votes',
            data: [Q4_A, Q4_B, Q4_C, Q4_D],
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
});


/* Chart.js | Chart for Question 4 */
const chart5 = document.getElementById('question5').getContext('2d');
const myChart5 = new Chart(chart5, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow'],
        datasets: [{
            label: '# of Votes',
            data: [Q5_A, Q5_B, Q5_C],
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
});