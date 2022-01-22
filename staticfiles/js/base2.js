
/* Chart.js */
/* Example on using Chart.js 
It appears the variable name of myChart, the second const, doesnt matter. */
const chart2 = document.getElementById('chartTwo').getContext('2d');
const myChart = new Chart(chart2, {
    type: 'pie',
    data: {
        labels: ['not legitimate'],
        datasets: [{
            label: '# of Votes',
            data: [3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
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