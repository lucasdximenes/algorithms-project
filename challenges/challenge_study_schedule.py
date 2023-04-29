def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    student_quantity = 0
    for period in permanence_period:
        if not (isinstance(period[0], int) and isinstance(period[1], int)):
            return None
        if period[0] <= target_time <= period[1]:
            student_quantity += 1

    return student_quantity
