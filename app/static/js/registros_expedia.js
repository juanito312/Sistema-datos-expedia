
//variables
let dataTable;
let dateTableIsInitialized = false;

const dataTableOptions = {
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dateTableIsInitialized) {
        dataTable.destroy();
    }

    await listExpedia();
    dataTable = $('#datatable-expedia').DataTable(dataTableOptions);

    dateTableIsInitialized = true;
};

const listExpedia = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_expedia");
        const data = await response.json();
        let content = ``;
        data.expedia.forEach((Expedia, index) => {
            content += `
                        <tr>
                            <td>${Expedia.srch_id}</td>
                            <td>${Expedia.site_id}</td>
                            <td>${Expedia.visitor_location_country_id}</td>
                            <td>${Expedia.visitor_hist_starrating}</td>
                            <td>${Expedia.visitor_hist_adr_usd}</td>
                            <td>${Expedia.prop_country_id}</td>
                            <td>${Expedia.prop_id}</td>
                            <td>${Expedia.prop_starrating}</td>
                            <td>${Expedia.prop_review_score}</td>
                            <td>${Expedia.prop_brand_bool}</td>
                            <td>${Expedia.prop_location_score1}</td>
                            <td>${Expedia.prop_location_score2}</td>
                            <td>${Expedia.price_usd}</td>
                            <td>${Expedia.promotion_flag}</td>
                            <td>${Expedia.srch_destination_id}</td>
                            <td>${Expedia.srch_length_of_stay}</td>
                            <td>${Expedia.srch_booking_window}</td>
                            <td>${Expedia.srch_adults_count}</td>
                            <td>${Expedia.srch_children_count}</td>
                            <td>${Expedia.srch_room_count}</td>
                            <td>${Expedia.srch_saturday_night_bool}</td>
                            <td>${Expedia.srch_query_affinity_score}</td>
                            <td>${Expedia.orig_destination_distance}</td>
                            <td>${Expedia.comp1_rate}</td>
                            <td>${Expedia.comp1_inv}</td>
                            <td>${Expedia.comp1_rate_percent_diff}</td>
                            <td>${Expedia.comp2_rate}</td>
                            <td>${Expedia.comp2_inv}</td>
                            <td>${Expedia.comp2_rate_percent_diff}</td>
                            <td>${Expedia.comp3_rate}</td>
                            <td>${Expedia.comp3_inv}</td>
                            <td>${Expedia.comp3_rate_percent_diff}</td>
                            <td>${Expedia.comp4_rate}</td>
                            <td>${Expedia.comp4_inv}</td>
                            <td>${Expedia.comp4_rate_percent_diff}</td>
                            <td>${Expedia.comp5_rate}</td>
                            <td>${Expedia.comp5_inv}</td>
                            <td>${Expedia.comp5_rate_percent_diff}</td>
                            <td>${Expedia.comp6_rate}</td>
                            <td>${Expedia.comp6_inv}</td>
                            <td>${Expedia.comp6_rate_percent_diff}</td>
                            <td>${Expedia.comp7_rate}</td>
                            <td>${Expedia.comp7_inv}</td>
                            <td>${Expedia.comp7_rate_percent_diff}</td>
                            <td>${Expedia.comp8_rate}</td>
                            <td>${Expedia.comp8_inv}</td>
                            <td>${Expedia.comp8_rate_percent_diff}</td>
                            <td>${Expedia.day}</td>
                            <td>${Expedia.month}</td>
                            <td>${Expedia.year}</td>
                    </tr>`;
        });
        //Mostramos el contenido en el cuerpo de la tabla
        tableBody_programmers.innerHTML = content;
    } catch (er) {
        console.log(er);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});