
select @country_id := country_id from countries where country_name = 'United Kingdom';
select @onekey_lab_id := laboratory_id from laboratories where laboratory_code='Demopharmalab';
select @lab_id := laboratory_id from laboratories where laboratory_code='Demopharmalab';
select @salesforce_id := salesforce_id from laboratory_salesforces where salesforce_external_id_1 = 'demopharmalabsf';



INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor86', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','BENJAMIN', 'PHILLIPS', 'Ophthalmology', 'PSI SERVICES III, INC', 'MANITOWOC', '54220', 'WUSM00340486', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor86';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor86', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00340486';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor22', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','JESSIE', 'HWANG', 'Geriatric Medicine', 'CATHOLIC CHARITIES OF THE DIOCESE OF SIOUX CITY IA INC', 'MENLO PARK', '94025', 'WUSR00012922', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor22';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor22', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00012922';	

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor16', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','ABDUL', 'KHALIQ', 'Cardiovascular Disease (Internal Medicine)', 'REGION II HUMAN SERVICES', 'WEST HARTFORD', '6107', 'WUSM00414116', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor16';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor16', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00012916';	

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor61', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','WILLIAM', 'AUSMUS', 'Family Medicine', 'BEN COHEN, PH.D., P.C.', 'SAINT PETERSBURG', '33710', 'WUSR00055561', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor61';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor61', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00055561';		

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor608', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','WILLIAM', 'HWANG', 'Allergy & Immunology', 'PSYCAMORE, LLC', 'LARGO', '33779', 'WUSR000555608', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor608';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor608', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR000555608';	

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor316', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','MICHAEL', 'DIESENHOUSE', 'Adult Nurse Practitioner', 'NORTHWEST DIRECTIONS - EAU CLAIRE', 'TUCSON', '85741', 'WUSM00174316', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor316';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor316', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00174316';	

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor715', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','MARK', 'YOUNG', 'General Practice (Family Medicine)', 'CRISIS INTERVENTION SPECIALIST', 'NORTH PLATTE', '69101', 'WUSM00015751', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor715';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor715', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00015751';	

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor304', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','JOHN', 'MEYER', 'Pulmonary Critical Care Medicine', '4U COUNSELING SERVICES INC', 'LOUISVILLE', '40206', 'WUSM00185304', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor304';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor304', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00185304';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor205', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','MAHSA', 'SALEHI', 'Family Nurse Practitioner', 'SUBURBAN MENTAL HEALTH ASSOCIATES', 'COLUMBIA', '21045', 'WUSM00612025', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor205';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor205', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00612025';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor971', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','DENISE', 'GIMBEL', 'Internal Medicine', 'UNITED HEALTH AND BEHAVIORAL SERVICES, LLC', 'MARSHALLTOWN', '50158', 'WUSR00013971', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor971';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor971', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00013971';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor974', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','DENISE', 'GIMBEL', 'Endocrinology, Diabetes and Metabolism (Internal Medicine)', 'NJ CENTER FOR THE HEALING ARTS, INC.', 'IOWA FALLS', '50126', 'WUSR00013974', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor974';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor974', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00013974';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor587', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','TEDD', 'PUCKETT', 'Internal Medicine', 'QUINCO CONSULTING CENTER INC', 'CHRISTIANSBURG', '24073', 'WUSM00464587', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor587';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor587', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00464587';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor215', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','SHARON', 'JOE', 'Emergency Medicine', 'GEORGE W. ACKLEY PH.D., P.C.', 'LA JOLLA', '92037', 'WUSR00048251', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor587';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor215', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00048251';	
-----------------------------------------------------------------------------------
INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor963', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','VINCENT', 'SARDI', 'Other Registered Nursing Specialty', 'COUNTY OF LOS ANGELES DEPARTMENT OF MENTAL HEALTH', 'TRENTON', '8690', 'WUSM00061963', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor963';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor963', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM00061963';	


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor130', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','DEBRA', 'VOGEL', 'Other Registered Nursing Specialty', 'HUMAN SERVICES, INC', 'CEDAR RAPIDS', '52401', 'WUSR00288130', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor130';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor130', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00288130';			


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor157', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','MELISSA', 'GREEN', 'Other Medical Specialty', 'CRESTWOOD BEHAVIORAL HEALTH, INC.', 'DAVENPORT', '52803', 'WUSR00288157', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor157';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor157', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00288157';			


INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor166', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','TRACY', 'SHIFFLETT', 'Radiology', 'FAMILY SERVICE AGENCY OF MARIN', 'WILLOUGHBY', '44094', 'WUSR00288166', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor166';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor166', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00288166';			

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor827', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','HANNAH', 'LARSEN', 'Psychiatry (Psychiatry & Neurology)', 'POST OAKS CARE CENTER INC', 'MALDEN', '2148', 'WUSM01016827', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor827';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor827', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSM01016827';	

INSERT INTO users (user_type, external_id_1, laboratory_id)
VALUES
('doctor','demopharmalabsf_doctor463', @onekey_lab_id);

INSERT INTO  doctors ( doctor_type, doctor_firstname, doctor_lastname, doctor_specialty_1, doctor_name_center, doctor_name_city, doctor_postalcode, onekey_id, user_id, country_id, laboratory_id)
SELECT 'ONEKEY','JANE', 'SIMINO', 'Other Registered Nursing Specialty', 'ASPEN POINTE HEALTH SERVICES', 'NEW HAVEN', '6510', 'WUSR00266463', u.user_id, @country_id, @onekey_lab_id
FROM users u 
WHERE u.external_id_1 = 'demopharmalabsf_doctor463';


INSERT INTO  doctors_extra_data ( doctor_external_id_1, doctor_external_id_2, doctor_external_id_3, doctor_extra_data, doctor_id, laboratory_id)
SELECT 'demopharmalabsf_doctor463', null, null, null, d.doctor_id, @lab_id
FROM doctors d 
WHERE d.onekey_id = 'WUSR00266463';	


