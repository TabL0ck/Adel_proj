$(document).ready(function () {

    "use strict";

    var options7 = {
        series: [{
            name: 'Series 1',
            data: [20, 100, 40, 30, 50, 80, 33],
        }],
        chart: {
            height: 350,
            type: 'radar',
        },
        dataLabels: {
            enabled: true
        },
        plotOptions: {
            radar: {
                size: 140,
                polygons: {
                    strokeColors: '#e9e9e9',
                    fill: {
                        colors: ['#f8f8f8', '#fff']
                    }
                }
            }
        },
        title: {
            text: 'Республика Адыгея'
        },
        colors: ['#FF4560'],
        markers: {
            size: 4,
            colors: ['#fff'],
            strokeColor: '#FF4560',
            strokeWidth: 2,
        },
        tooltip: {
            y: {
                formatter: function (val) {
                    return val
                }
            }
        },
        xaxis: {
            categories: ['Образование', 'Дети', 'СП', 'Ученые степени', 'Мужчины', 'Женщины']
        },
        yaxis: {
            tickAmount: 7,
            labels: {
                formatter: function (val, i) {
                    if (i % 2 === 0) {
                        return val
                    } else {
                        return ''
                    }
                }
            }
        }
    };

    var chart7 = new ApexCharts(document.querySelector("#apex7"), options8);
    chart7.render();


    new Chart(document.getElementById("chartjs1"), { "type": "line", "data": { "labels": ["January", "February", "March", "April", "May", "June", "July"], "datasets": [{ "label": "My First Dataset", "data": [65, 59, 80, 81, 56, 55, 40], "fill": false, "borderColor": "rgb(75, 192, 192)", "lineTension": 0.1 }] }, "options": {} });

    new Chart(document.getElementById("chartjs2"), { "type": "bar", "data": { "labels": ["January", "February", "March", "April", "May", "June", "July"], "datasets": [{ "label": "My First Dataset", "data": [65, 59, 80, 81, 56, 55, 40], "fill": false, "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(255, 159, 64, 0.2)", "rgba(255, 205, 86, 0.2)", "rgba(75, 192, 192, 0.2)", "rgba(54, 162, 235, 0.2)", "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"], "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)", "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"], "borderWidth": 1 }] }, "options": { "scales": { "yAxes": [{ "ticks": { "beginAtZero": true } }] } } });

    new Chart(document.getElementById("chartjs3"), { "type": "radar", "data": { "labels": ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"], "datasets": [{ "label": "My First Dataset", "data": [65, 59, 90, 81, 56, 55, 40], "fill": true, "backgroundColor": "rgba(255, 99, 132, 0.2)", "borderColor": "rgb(255, 99, 132)", "pointBackgroundColor": "rgb(255, 99, 132)", "pointBorderColor": "#fff", "pointHoverBackgroundColor": "#fff", "pointHoverBorderColor": "rgb(255, 99, 132)" }, { "label": "My Second Dataset", "data": [28, 48, 40, 19, 96, 27, 100], "fill": true, "backgroundColor": "rgba(54, 162, 235, 0.2)", "borderColor": "rgb(54, 162, 235)", "pointBackgroundColor": "rgb(54, 162, 235)", "pointBorderColor": "#fff", "pointHoverBackgroundColor": "#fff", "pointHoverBorderColor": "rgb(54, 162, 235)" }] }, "options": { "elements": { "line": { "tension": 0, "borderWidth": 3 } } } });

    new Chart(document.getElementById("chartjs4"), { "type": "doughnut", "data": { "labels": ["Red", "Blue", "Yellow"], "datasets": [{ "label": "My First Dataset", "data": [300, 50, 100], "backgroundColor": ["rgb(255, 99, 132)", "rgb(54, 162, 235)", "rgb(255, 205, 86)"] }] } });

});
