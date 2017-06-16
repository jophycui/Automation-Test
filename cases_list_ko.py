from test_cases import exam_math_g1
from test_cases import exam_math_g3
from test_cases import exam_physics_g1
from test_cases import exam_physics_g3
from test_cases import exam_random_cs_g1
from test_cases import exam_faculty_cn




def case_list():
    alltestcases = [
        exam_math_g1.Math_G1,
        # exam_physics_g1.Physics_G1,
        # exam_physics_g3.Physics_G3,
        # exam_math_g3.Math_G3,
        # exam_math_physics_g1.MathPhysics_G1
        #exam_creativity.Creativity
        #exam_ct.CT
        #exam_ql.QL
        #exam_random_cs_g1.Random_CS_G1




    ]
    print "....Get all test cases...."
    return alltestcases

