def schedule_vehicles(vehicles, total_hours):

    for vehicle in vehicles:
        vehicle["score"] = (
            vehicle["priority"] / vehicle["maintenance_hours"]
        )

    vehicles.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    scheduled = []
    used_hours = 0

    for vehicle in vehicles:

        if used_hours + vehicle["maintenance_hours"] <= total_hours:

            scheduled.append(vehicle)
            used_hours += vehicle["maintenance_hours"]

    return {
        "scheduled_vehicles": scheduled,
        "used_hours": used_hours,
        "remaining_hours": total_hours - used_hours
    }