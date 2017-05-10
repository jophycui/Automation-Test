class AccessInfo(object):
    math_g1_student_id = 'math1ko6'
    math_g1_token = 'math1ko'
    physics_g1_student_id ='phys1ko16'
    physics_g1_token = 'phys1ko'
    math_g3_student_id = 'math3ko3'
    math_g3_token = 'math3ko'
    physics_g3_student_id ='phys3ko9'
    physics_g3_token = 'phys3ko'
    random_student_id = 'random2017G3ko2'
    random_token = 'tokenko'
    cr_student_id = 'creac4'
    cr_token = 'creac'
    ct_student_id = 'critko3'
    ct_token = 'critko'

    test_id =[math_g1_student_id, physics_g1_student_id, math_g3_student_id, physics_g3_student_id, cr_student_id, ct_student_id, random_student_id]


class RandomExamPath(object):
    G1EE_RR_CR = ('email', 'RR-G4_EN', 'MATH-G1_ENG', 'Q-G1-HOT')
    G1EE_PM = ('email', 'PHYS-G1_ENG', 'MATH-G1_ENG', 'Q-G1-MP')
    G1EE_MP = ('email', 'MATH-G1_ENG', 'PHYS-G1_ENG', 'Q-G1-MP')
    G1CS_CQ = ('email', 'CT-G4_KO_Sample', 'CT-G4_KO', 'QL_KO_Sample', 'QL_KO', 'CR-G4_KO_part1', 'CR-G4_KO_part2', 'Q-G1-HOT')
    G1CS_PM = ('email', 'PHYS-G1_ENG', 'MATH-G1_ENG', 'Q-G1-MP')
    G1CS_MP = ('email', 'MATH-G1_ENG', 'PHYS-G1_ENG', 'Q-G1-MP')