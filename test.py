import unittest
from proximity import proximity



"""
TestProximity class

This class use unittest python library doing test, it print the input and the expected output, it provides some text sample 
and some query sample.


test_proximity(self):
    use unittest, print the output in red if some test are not passed
    
proximity_output(self):
    print input, output in a human readable form
"""

class TestProximity(unittest.TestCase):
    #Text from Challenge
    t1 = """
            Continental does not have an office in Zürich.
            """
    t2 = """
             The Burke County location of Continental is a division of a larger
            corporation with sales of around $46 billion in 2013. Continental is among
            the leading automotive suppliers worldwide. As a supplier of brake
            systems, systems and components for powertrains and chassis,
            instrumentation, infotainment solutions, vehicle electronics, tires, and
            technical elastomers, Continental contributes to enhanced driving safety
            and global climate protection.  Continental is also an expert partner in
            networked automobile communication.  Continental currently employs around
            178,000 people in 49 countries. The two Morganton facilities are part of
            the Vehicle Dynamics Business Unit, which is one of four Business Units
            within Continental."""
    t3 = """
            We are proud of our company, our products and our facilities,” said Naomi
            Cole, senior human resource manager for Continental Automotive Systems in
            Morganton. “Each of us has an important job to do, and ultimately the
            success of our company depends upon how well we individually and
            collectively perform our jobs and ultimately satisfy our customers. We
            seek employees who have the ability to contribute toward our success in a
            meaningful way. It is the success of our company as a profitable business
            that will increase our job security, opportunities for personal growth,
            and support Burke and the surrounding counties.
            """

    t4 = """
            The report reveals that Bridgestone, Michelin, Goodyear, Pirelli and
            Continental are few of the dominant tyre manufacturers in the UAE,
            accounting for a substantial share in the country's tyre market. These
            leading players are constantly growing due to their well-established
            supply chain network, comprising exclusive distributorships and local
            dealers.
            """


    #Text to try accuracy in strange situations
    t5 = """
            This is a brown dog"""

    t6 = """
            This dog is really brown
            """
    t7 = """
            The dog is brown but this document is very very long
            """
    t8= """
            The dog is red but the fox is brown"
    """

    q1 = """Continental"""
    q2 = """Continental Breakfast in Zürich"""

    q3 = """Continental Automotive Systems, Inc. in Morgaton, NC"""
    q4 = """This is not a system"""

    q5 = """brown"""
    q6 = """dog is brown"""
    q7 = """brown dig"""
    q8 = """dog long"""
    q9= """Morganon"""


    results = (
        #Word continental is in all 4 text
        (q1, t1, True),
        (q1, t2, True),
        (q1, t3, True),
        (q1, t4, True),
        #Word breakfast is not present near continental
        (q2,t1,False),
        (q2,t2,False),
        (q2,t3,False),
        (q2,t4,False),

        #Continental Automotive Systems, Inc. in Morgaton, NC"
        (q3,t1,False),
        (q3,t2,False),
        (q3,t3,True),
        (q3,t4,False),

        #this is not a system
        (q4, t1, False),
        (q4, t2, False),
        (q4, t3, False),
        (q4, t4, False),


        #Importance tests

        #Proximity very high, higher when there are more words
        (q5,t5,True),
        (q5,t6,True),
        (q5,t7,True),

        #With three words still high accuracy
        (q6,t5,True),
        (q6,t6,True),
        (q6,t7,True),

        #Misspelling >10% of the word, everything should be false
        (q7,t5,False),
        (q7,t6,False),
        (q7,t7,False),
        (q7,t8,False),

        # Misspelling <10% of the word, everything should be True
        (q9,t3,True),

        #if the words are far apart should be false
        (q8,t5,False),
        (q8,t6,False),
        (q8,t7,False)
    )





    def test_proximity(self):
        for r in range(len(self.results)):

            result=self.results[r]

            with self.subTest(msg="test_proximity of "+result[0]+" in "+result[1] ):

                output=proximity(result[1],result[0])

                self.assertEqual(output[0], result[2])

    def proximity_output(self):
        for r in range(len(self.results)):

            result=self.results[r]
            output = proximity(result[1], result[0])
            print("\nQuery \"" + result[0] + "\"" + " in text " + result[1])
            print("\nReturn Value: ", output)
            print("="*50 )




if __name__ == '__main__':
    TestProximity.proximity_output(TestProximity);
    print("\n\n")
    unittest.main()
