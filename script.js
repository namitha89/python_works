// Here You can type your custom JavaScript...
// Here You can type your custom JavaScript...// --------------------------------------------------------------------
// --------------------------------------------------------------------
// configuration starts

// time_slots_to_open open any one active link only
time_slots_to_open = 1

// Set date_selection_descending to 1 to select from last else set 0 to select first
date_selection_descending = 1

// Always remember to update this
// Always use this format_date
// Eg: appointment_start_date = "10.07.2019"

appointment_start_date = "15.08.2019"
appointment_end_date = "10.09.2019"

// configuration ends
// --------------------------------------------------------------------

// code code code code code code code code code code code code code code

if (window.location.pathname.search('appointment_showForm') != -1) {
  ele = document.getElementsByTagName('captcha')[0]
  kk = ele.children[0]
  kk.style['height'] = '88px'
  kk.style['background-size'] = 'contain'
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  inpp = $("#appointment_newAppointmentForm_captchaText")[0]
  inpp.focus()
}

if (window.location.pathname.search('appointment_showMonth') != -1) {

  ele = document.getElementsByTagName('captcha')[0]
  /*
    kk = ele.children[0]
    kk.style['height'] = '88px'
    kk.style['background-size'] =  'contain'
    */

  if (ele) {
    inpp = $("#appointment_captcha_month_captchaText")[0]
    inpp.focus()
  }
}



console.log('loadedd')
window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);


// CODE FOR MONTH SELECTION LOGIC
// CODE FOR MONTH SELECTION LOGIC
// CODE FOR MONTH SELECTION LOGIC
// CODE FOR MONTH SELECTION LOGIC
// CODE FOR MONTH SELECTION LOGIC


function format_date(d_str) {
  return new Date(d_str.replace(/(\d{2}).(\d{2}).(\d{4})/, "$2/$1/$3"))
}


function open_href_async(href, delay = 00) {
  if (href != null) {
    setTimeout(function(href) {
      window.open(href);
    }, delay, href);
  } else {
    console.log("null URL to open")
  }
}



function has_link(test_div) {
  return test_div.children[1].children[0].tagName.toLowerCase() == 'a'
}


function filter_interested_divs(divs, from_dt_str, to_dt_str) {
  var filterd = []
  var from_dt = format_date(from_dt_str)
  var to_dt = format_date(to_dt_str)

  divs.forEach(function(div) {
    if (div.children.length != 0) {
      appointment_date_str = div.children[0].textContent.split(' ')[1].replace(/(\r\n|\n|\r|\t)/gm, "")
      appointment_date = format_date(appointment_date_str)
      // Check if the div has link in It
      // Check if the div also is in range of start and end date
      if ((has_link(div) == true) && (appointment_date >= from_dt) && (appointment_date <= to_dt)) {
        filterd.push(div);
        console.log("pushing "+ appointment_date)
      }

    }
  });

  return filterd
}


function get_preffered_day_selection_href() {
  appointment_days = $('.wrapper div[style="width: 100%;"]').toArray();
  filterd_divs = filter_interested_divs(appointment_days, appointment_start_date, appointment_end_date)
  if (filterd_divs.length != 0) {
    if(date_selection_descending == 1) {
      day_div_selected = filterd_divs.length-1;
    }else{
      day_div_selected = 0;
    }
    return filterd_divs[day_div_selected].children[1].children[0].href
  }
  return null;
}



// // open timeslot appointment for the month
count = 0
if (window.location.pathname.search("appointment_showMonth") != -1) {
  href = get_preffered_day_selection_href()
  open_href_async(href)
}

// CODE FOR DAY SPECIFIC SELECTION
// CODE FOR DAY SPECIFIC SELECTION
// CODE FOR DAY SPECIFIC SELECTION
// CODE FOR DAY SPECIFIC SELECTION
// CODE FOR DAY SPECIFIC SELECTION
// CODE FOR DAY SPECIFIC SELECTION

function get_smart_timeslot_selection_index() {
  timeslots_slots_divs = $('.wrapper div[style="width: 100%;"]')

  function get_available_appointments(appoints_per_slots) {
    if (appoints_per_slots != null && appoints_per_slots.length != 0) {
      try {
        return appoints_per_slots.map(Number)[0]
      } catch (err) {
        return 0
      }
    }
  }

  appointments_availability_order = []

  timeslots_slots_divs.toArray().slice(1,).forEach(function(div_ele, i) {
    appoints_per_slots = div_ele.children[1].textContent.match(/\d+/g)
    appointments_availability_order.push([i, get_available_appointments(appoints_per_slots)])
  })


  appointments_availability_order = appointments_availability_order.sort(function(a, b) {
    return a[1] - b[1];
  })

  smart_selection_index = appointments_availability_order[appointments_availability_order.length-1][0]
  return smart_selection_index;
}



// open day slot appointment for the day
dayCount = 0
if (window.location.pathname.search("appointment_showDay") != -1) {
  try {
    // open the time slot by looking at the max appointments available
    // for a given time slots
    // Skip the first anchor as its show month
    available_day_slots = $('a.arrow[onclick="return startCommitRequest();"]').toArray().slice(1,)
    smart_selection_index = get_smart_timeslot_selection_index()
    console.log(available_day_slots[smart_selection_index])

    open_href_async(available_day_slots[smart_selection_index].href)

  } catch (err) {
    // if any error open the last one
    console.log(err)
    open_href_async(available_day_slots.reverse()[0].href);
  }
}