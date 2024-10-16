// static/js/charts.js

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',  // You can change to 'pie', 'line', etc.
    data: {
        labels: ['Village 1', 'Village 2', 'Village 3'],  // Placeholder data
        datasets: [{
            label: '# of Surveys',
            data: [12, 19, 3],  // Placeholder data
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(75, 192, 192, 1)'
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
