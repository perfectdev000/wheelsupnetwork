
/**
 * pageTrackGA - Track the page view using Google Analytics
 * @param {*} ga - Google Analytics instantes
 * @param {string} page - Name of the page to track
 * @param {string} title - Title of the page to track
 * @param {string} location - Location (href) of the page to track
 */
export function pageTrackGA(ga, page, title, location) {
    ga.page({page, title, location})
}

/**
 * screenViewGA - Track the a screenview event using Google Analytics
 * @param {*} ga - Google Analytics instantes
 * @param {string} screenName - Name of the screenName event to track
 */
export function screenViewGA(ga, screenName) {
    ga.screenview({screenName})
}

/**
 * pageTrackGAV4 - Track the page view using Google Analytics V4
 * @param {*} gtag - Google Analytics instantes
 * @param {string} page_path - Name of the page to track
 * @param {string} page_title - Title of the page to track
 * @param {string} page_location - Location (href) of the page to track
 */
 export function pageTrackGAV4(gtag, page_path, page_title, page_location) {
    gtag.pageview({page_path, page_title, page_location})
}

/**
 * screenViewGAV4 - Track the a screenview event using Google Analytics V4
 * @param {*} gtag - Google Analytics instantes
 * @param {string} screen_name - Name of the screen to track
 * @param {string} app_name - Name of app being tracked
 */
export function screenViewGAV4(gtag, screen_name, app_name) {
    gtag.screenview({app_name, screen_name})
}