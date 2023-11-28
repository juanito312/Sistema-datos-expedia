// Recuperar los datos de Django y convertirlos a formato adecuado para C3.js
let datos8 = JSON.parse('{{ datos_expedia_json8| safe }}');

// Verificar si 'srch_saturday_night_bool' está definido y no es nulo
if (datos8 && datos8[0] && datos8[0]['srch_saturday_night_bool']) {
    // Obtener los valores y las etiquetas para el gráfico de barras
    let estadiaSabado = datos8.map(item => String(item['srch_saturday_night_bool']));
    let numReservas8 = datos8.length;  // Utilizar la longitud de los datos para representar el número de hoteles

    // Configuración e inicialización del gráfico con C3.js
    var chart = c3.generate({
        bindto: '#miGrafica8',
        data: {
            y: 'Inclusion de sabado en la Estadia',
            columns: [
                ['Inclusion de sabado en la Estadia'].concat(estadiaSabado),
                ['Numero de Reservas'].concat(numReservas8)
            ],
            type: 'area'

        },
        axis: {
            x: {
                type: 'category',
                label: 'Inclusion de sabado en la Estadia'
            },
            y: {
                label: 'Numero de Reservas'
            }
        },
        title: {
            text: 'Proporcion de Estadia con y sin sabado'
        }
    });
}