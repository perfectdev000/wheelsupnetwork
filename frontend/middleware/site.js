const axios = require("axios");

export default async function validatedSite({ $config }) {
  const { data } = await axios.get(
    `https://api.ipstack.com/check?access_key=${$config.ipstack}`
  );
  
  // Do not show content from usa to cuba, and change of content to canada
  if($config.siteUid == 'wheels-up-network'){
    $config.siteUid = data.country_name == "Canada" || data.country_name == "Cuba"
    ? "wheels-up-network-canada"
    : "wheels-up-network-usa"
  }

  if (!isWhiteList(data)) {
    // get host this country
    const host = getHostThisCountry(data.country_name)

     
    // delete www. to host
    const getHost = window.location.host.replace("www.", "")
 
    // Get the domain name
    const hostName = getHost.split(".");
    // only for Latin American site
    redirectionHost(host, getHost, hostName[0]);
  }
}

const getHostThisCountry = (country) => {
  let sites = {
    Argentina: "soloparaagentes.ar",
    Colombia: "soloparaagentes.co",
    Mexico: "soloparaagentes.mx",
    Bolivia: "soloparaagentes.co",
    Chile: "soloparaagentes.ar",
    Ecuador: "soloparaagentes.co",
    Guyana: "soloparaagentes.co",
    "Guyana Francesa": "soloparaagentes.co",
    Paraguay: "soloparaagentes.co",
    Peru: "soloparaagentes.co",
    Suriname: "soloparaagentes.co",
    Uruguay: "soloparaagentes.ar",
    Venezuela: "soloparaagentes.co",
    Belice: "soloparaagentes.mx",
    "Costa Rica": "soloparaagentes.mx",
    "El Salvador": "soloparaagentes.co",
    Guatemala: "soloparaagentes.mx",
    Honduras: "soloparaagentes.mx",
    Nicaragua: "soloparaagentes.mx",
    Panamá: "soloparaagentes.mx",
    Spain: "soloparaagentes.com",
    Canada: "wheelsupnetwork.ca"
  };
  return sites[country];
};
const redirectionHost = (host, getHost, hostName) => {
  if(host === "wheelsupnetwork.ca" && !getHost.includes("wheelsupnetwork.ca")) {
    return window.location.replace("https://" + host);
  }
  if (hostName === "soloparaagentes") {
    if (host === undefined && getHost != "soloparaagentes.com")
      return window.location.replace("https://soloparaagentes.com");
    else if (host === undefined) {
      return false;
    }
    else if (getHost != host) {
      return window.location.replace("https://" + host);
    }
  }
};

const isWhiteList = ({ ip }) => {
  let whitelist = {
    '62.171.152.48': true,
    '189.174.217.79': true
  };
  return whitelist[ip] ? true : false;
};
