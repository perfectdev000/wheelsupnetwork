import Vue from "vue";

Vue.filter("truncate", (string, limit) => {
  return string.length > limit ? string.substr(0, limit - 1) + "..." : string;
});

Vue.filter("formateDate", (value, locale) => {
    // format date
    let date  = new Date(value);
    // get months
    var mount = mounts[locale][date.getMonth()];
    // get day
    var day   = days[locale][date.getDay()];
     // get date & add 0 
    var dateNumber = date.getDate() < 10 ? `0${date.getDate()}` : date.getDate();
    // year
    var year = date.getFullYear();
    // language formt
    if (locale == "es") return `${day}, ${dateNumber} de ${mount} de ${year}`;
    else return `${mount} ${dateNumber}, ${year}`;
});

const days = {
  es: {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
  },
  en: {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
  },
};

const mounts = {
  es: {
    0: "Ene",
    1: "Feb",
    2: "Mar",
    3: "Abr",
    4: "May",
    5: "Jun",
    6: "Jul",
    7: "Ago",
    8: "Sep",
    9: "Oct",
    10: "Nov",
    11: "Dic",
  },
  en: {
    0: "Jan",
    1: "Feb",
    2: "Mar",
    3: "Apr",
    4: "May",
    5: "Jun",
    6: "Jul",
    7: "Aug",
    8: "Sep",
    9: "Oct",
    10: "Nov",
    11: "Dec",
  },
};
