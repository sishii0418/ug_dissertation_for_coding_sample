** Merge dta's from January 1994, only those who are unemployed

use "/mnt/e/dissertation_2425/data/CPS_from_1989/cpsb199401.dta", clear
keep if prempnot == 2

* Define the start date and end date.
global start = ym(1994, 2)
global end = ym(2024, 12)

* Loop through each month between the start and end dates, inclusive.
forval each = $start/$end {
	local month = dofm(`each')
	local y = year(`month')
        local m = month(`month')
	local formatted_date = string(`y', "%04.0f") + string(`m', "%02.0f")
	** display `formatted_date'
	append using "/mnt/e/dissertation_2425/data/CPS_from_1989/cpsb`formatted_date'.dta"
	keep if prempnot == 2
}
