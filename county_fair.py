class Attraction:
    def __init__(self, name, location, capacity, operating_hours, age_restrictions):
        self.name=name
        self.location=location
        self.capacity=capacity
        self.operating_hours=operating_hours
        self.age_restrictions=age_restrictions



    def attracton_name_and_location(self):
        print("the {self.name} attraction is at {self.location}")
        
    def attracton_capacity_and_age_restrictions(self):
        print("the attraction has {self.capacity} places and the minimum age is {self.age_restrictions}")
      
              
class Show(Attraction):
    def __init__(self, name, location, capacity, operating_hours, age_restrictions,performances_type, duration, schedule, performer_names): 
        super().__init__(self, name, location, capacity, operating_hours, age_restrictions)
        self.performances_type=performances_type
        self.duration=duration
        self.schedule=schedule
        self.performer_names=performer_names
        
    def date_hours_informations(self):
        print("the show start {self.schedule} and the duration is {self.duration}")
     
             
class Ride(Attraction):
    def __init__(self, name, location, capacity, operating_hours, age_restrictions, ride_type, height_requirement, speed, duration): 
        super().__init__(self, name, location, capacity, operating_hours, age_restrictions)
        self.ride_type=ride_type
        self.height_requirement=height_requirement
        self.speed=speed
        self.duration=duration
              
class Booth(Attraction):
    def __init__(self, name, location, capacity, operating_hours, age_restrictions, booth_type,number_of_workers, product_service_offered, queue_capacity): 
        super().__init__(self, name, location, capacity, operating_hours, age_restrictions)
        self.booth_type=booth_type
        self.number_of_workers=number_of_workers
        self.product_service_offered=product_service_offered
        self.queue_capacity=queue_capacity 
        
#############################


class Vendor:
    def __init__(self,name, location, vendor_type, permit_status, revenue):
        self.name=name
        self.location=location
        self.vendor_type=vendor_type
        self.permit_status=permit_status
        self.revenue=revenue

class Food(Vendor):
    def __init__(self,name, location, vendor_type, permit_status, revenue,cuisine_type,health_inspection_status,menu_offering):
        super().__init__(self,name, location, vendor_type, permit_status, revenue)
        self.cuisine_type=cuisine_type
        self.health_inspection_status=health_inspection_status
        self.menu_offering=menu_offering 

class Merchandise(Vendor):
    def __init__(self,name, location, vendor_type, permit_status, revenue,product_type,stock_quantity,pricing):
        super().__init__(self,name, location, vendor_type, permit_status, revenue)
        self.product_type=product_type
        self.stock_quantity=stock_quantity
        self.pricing=pricing

class Service(Vendor):
    def __init__(self,name, location, vendor_type, permit_status, revenue,service_type,required_equipement,staff_count):
        super().__init__(self,name, location, vendor_type, permit_status, revenue)
        self.service_type=service_type
        self.required_equipement=required_equipement
        self.staff_count=staff_count

class Entertainment(Vendor):
    def __init__(self,name, location, vendor_type, permit_status, revenue,act_type,performance_duration,audience_capacity):
        super().__init__(self,name, location, vendor_type, permit_status, revenue)
        self.act_type=act_type
        self.performance_duration=performance_duration
        self.audience_capacity=audience_capacity

#############################

class Map:
    def __init__(self,layout_design, entry_points, major_attractions, vendor_locations):
        self.layout_design=layout_design
        self.entry_points=entry_points
        self.major_attractions=major_attractions
        self.vendor_locations=vendor_locations
        

#############################

class Admissions:
    def __init__(self,ticket_price, payment_methods, daily_visitor_count, pass_options):
        self.ticket_price=ticket_price
        self.payment_methods=payment_methods
        self.daily_visitor_count=daily_visitor_count
        self.pass_options=pass_options
 

#############################

class Schedule:
    def __init__(self,event_list, start_times, locations, duration):
        self.event_list=event_list
        self.start_times=start_times
        self.locations=locations
        self.duration=duration

    
