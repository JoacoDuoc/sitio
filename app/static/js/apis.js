const apiUrl = 'https://api.exchangerate-api.com/v4/latest/USD';

async function fetchExchangeRates() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        const usdRateCLP = data.rates.CLP;
        document.getElementById('dolar-clp').innerText = `Dólar (USD) en CLP: ${usdRateCLP}`;


        const euroRateUSD = data.rates.EUR;
        const euroRateCLP = euroRateUSD * usdRateCLP;
        document.getElementById('euro-clp').innerText = `Euro (EUR) en CLP: ${euroRateCLP}`;
    } catch (error) {
        console.error('Error al obtener los datos de conversión de moneda:', error);
    }
}

fetchExchangeRates();
