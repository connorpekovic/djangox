$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

/* Privatley receieve the conext data to use in JavaScript  */
const Q1_A = JSON.parse(document.getElementById('Q1_A').textContent);
const Q1_B = JSON.parse(document.getElementById('Q1_B').textContent);
const Q1_C = JSON.parse(document.getElementById('Q1_C').textContent);



/* Chart.js */
/* Example on using Chart.js 
It appears the variable name of myChart, the second const, doesnt matter. */
const chart1 = document.getElementById('question1').getContext('2d');
const myChart = new Chart(chart1, {
    type: 'pie',
    data: {
        labels: ['Humans', 'Alien Intervention', 'Divine Intervention'],
        datasets: [{
            label: '# of Votes',
            data: [Q1_A, Q1_B, Q1_C],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
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
