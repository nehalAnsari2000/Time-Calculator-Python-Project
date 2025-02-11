def add_time(start, duration, weekdays = ''):

  # Initializing some variable for final result
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  h_final, m_final, ap_final, n, day_final = 0, 0, '', 0, ''   

  # Extracting hours, minutes ans AM/PM from start time
  h_start = start.split(' ')[0].split(':')[0]
  m_start = start.split(' ')[0].split(':')[1]         
  ap_start = start.split(' ')[1]

  # Extracting hours, minutes from duration to add
  h_duration = duration.split(':')[0]
  m_duration = duration.split(':')[1]

  if int(m_duration) > 60 :         # Checking for invalid minutes
    return 'Invalid minutes!'

  # Main logic starts from here
  if int(h_duration) >= 24:
    n = int(h_duration) // 24
    h_duration = int(h_duration) % 24

  h_final = int(h_start) + int(h_duration)
  m_final = int(m_start) + int(m_duration)

  if m_final >= 60:
    m_final = m_final % 60
    h_final += 1

  if h_final >= 12:
    if h_final == 12:
      rem = 12
    else:
      rem = h_final % 12

    h_final = rem
    if ap_start == 'PM':
      n += 1
    ap_final = 'AM' if ap_start == 'PM' else 'PM'
  else:
    ap_final = ap_start

  if len(weekdays) > 0:
    day_index = days.index(weekdays.lower())

  # Returning formatted final output string
  if n == 0:
    if len(weekdays) > 0:
      return f"{h_final}:{m_final:02d} {ap_final}, {weekdays.title()}"
    else:
      return f"{h_final}:{m_final:02d} {ap_final}"
  elif n == 1:
    if len(weekdays) > 0:
      return f"{h_final}:{m_final:02d} {ap_final}, {days[(day_index+n)%7].title()} (next day)"
    else:
      return f"{h_final}:{m_final:02d} {ap_final} (next day)"
  else:
    if len(weekdays) > 0:
      return f"{h_final}:{m_final:02d} {ap_final}, {days[(day_index+n)%7].title()} ({n} days later)"
    else:
      return f"{h_final}:{m_final:02d} {ap_final} ({n} days later)"

  # return new_time
print(add_time('8:16 PM', '466:02', 'tuesday'))