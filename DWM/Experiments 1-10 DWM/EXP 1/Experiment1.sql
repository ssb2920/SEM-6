/* CLASS   : TE COMPUTERS batch A*/
/* TOPIC   : EXPERIMENT 1 SQL CODE */



CREATE TABLE dimtime(
	time_key VARCHAR(3) PRIMARY KEY,
	day NUMERIC(2),
	day_of_week VARCHAR(10),
    month VARCHAR(10),
    quarter NUMERIC(1),
    year NUMERIC(4)
	
);


INSERT INTO dimtime(time_key,day,day_of_week,month,quarter,year)VALUES
(t1,1,monday,january,1,2019),
(t2,2,tuesday,april,2,2019),
(t3,3,wednesday,july,3,2019),
(t4,4,thursday,august,3,2019),
(t5,5,friday,november,4,2019);

/*--------------------------------X------------------------------*/


CREATE TABLE dimpatient(
	patient_id VARCHAR(3) PRIMARY KEY,
	patient_name VARCHAR(30),
	phone_number NUMERIC(10),
	sex VARCHAR(1),
    description VARCHAR(50),
    address VARCHAR(50)

);



INSERT INTO dimpatient(patient_id,patient_name,phone_number,sex,description,address)VALUES
	(p1,jean,9967040892,F,healthy,bandra),
    (p2,jane,9967040893,F,diabetic,khar),
    (p3,joan,9967040894,F,hypertension,worli),
    (p4,john,9967040895,M,obesity,juhu),
    (p5,james,9967040896,M,gout,colaba);

/*--------------------------------X------------------------------*/




CREATE TABLE dimdoctor(
	doctor_id VARCHAR(3) PRIMARY KEY,
    doctor_name VARCHAR(30),
    phone_number NUMERIC(10),
    sex VARCHAR(1),
    address VARCHAR(50)
);



INSERT INTO dimstore(doctor_id,doctor_name,phone_number,sex,address)VALUES
 (d1,pete,9820323412,M,bandra),
 (d1,peter,9820323413,M,khar),
 (d1,pedro,9820323414,M,worli),
 (d1,petra,9820323415,F,juhu),
 (d1,pedra,9820323416,F,colaba);
/*--------------------------------X------------------------------*/


CREATE TABLE factdata(
    time_key VARCHAR(3) REFERENCES dimtime(time_key),
    patient_id VARCHAR(3) REFERENCES dimpatient(patient_id),
    doctor_id VARCHAR(3) REFERENCES dimdoctor(doctor_id),
    charge NUMERIC(30),
    count NUMERIC(30)
);

INSERT INTO factsales (time_key,patient_id,doctor_id,charge,count) VALUES
    (t1,p1,d1,1000,1);
    (t2,p2,d2,1500,2);
    (t3,p3,d3,2000,1);
    (t4,p4,d4,2500,2);
    (t5,p5,d5,3000,1);

/*--------------------------------X------------------------------*/
