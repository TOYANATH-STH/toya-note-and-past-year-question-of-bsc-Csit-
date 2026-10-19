import re

with open(r'C:\Users\Ritesh Shrestha\toya-bsc-csit\sem6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New Technical Writing PYQ section
new_tw_section = '''    <div class="content-section">
      <div class="content-header">
        <a href="sem6.html" class="back-link">&#8592; Back to Semester VI</a>
        <h2>Technical Writing &mdash; Past Year Questions</h2>
      </div>
      <div class="content-actions">
        <button class="btn btn-download">&#128466; Download PYQ PDF</button>
      </div>
      <div class="content-body">
        <!-- ===== 2082-new Board ===== -->
        <a id="board-tw-2082new"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>Technical Writing &mdash; 2082-new Board</strong>
            <span class="pyq-meta">Full Marks: 80 + 20 &nbsp;|&nbsp; Pass Marks: 32 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Long Answer Questions (Attempt any TWO)</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Explain the concept of audience analysis in technical writing. Develop an audience profile for a user manual of a mobile banking application.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">Discuss the writing process for technical documents. Illustrate each stage with relevant examples from IT workplace writing.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">What role do document design principles play in technical communication? Explain with examples.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Short Answer Questions (Attempt any EIGHT)</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Differentiate technical writing from creative writing.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">What is an abstract? Write an informative abstract for a report on &lsquo;Cybersecurity Awareness among Campus Students&rsquo;.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Explain the importance of ethics in workplace communication.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Write a short news release announcing the launch of a new cloud-based student portal.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Describe the significance of graphics in presenting numerical data.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">Prepare a memo instructing staff to shift to a new digital attendance system.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">What are the characteristics of an effective presentation?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Make a flow-chart diagram of your dream application.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on:</span><span class="pyq-marks">5</span><p class="pyq-short-note">a. Flowchart</p><p class="pyq-short-note">b. Web Page Layout</p></div>
          </div>
        </div>

        <!-- ===== 2082 Board ===== -->
        <a id="board-tw-2082"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>Technical Writing &mdash; 2082 Board</strong>
            <span class="pyq-meta">Full Marks: 80 + 20 &nbsp;|&nbsp; Pass Marks: 32 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any THREE questions</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">What is a recommendation report and how does it differ from a proposal? Your IT consulting firm has been asked by a client to evaluate three different cloud storage solutions (Google Drive, Dropbox, and Microsoft OneDrive) and recommend the best option for their 50-employee business. Write a recommendation report that includes problem statement, evaluation criteria, detailed analysis of each option, and your recommendation with proper justification.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">Explain the complete technical writing process from planning to publishing. How does collaborative writing enhance or complicate this process? Discuss the advantages, challenges, and conflict resolution strategies in collaborative writing. Support your answer with examples from software documentation or IT project scenarios.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">You are working as a web content manager for a software development company in Nepal. Your company wants to redesign its website to improve user experience, accessibility, and search engine visibility. Write a comprehensive proposal addressing: (a) Key principles for organizing and designing web pages, (b) Best practices for writing effective web content, (c) Information architecture considerations, (d) How to ensure web accessibility for users with disabilities. Include specific examples relevant to a tech company.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Discuss the importance of ethics in technical writing and workplace communication. What ethical dilemmas might technical writers face in the IT industry? Explaxain the steps a technical writer should take when confronted with ethical issues such as inaccurate information, plagiarism, or organizational wrongdoing. How can organizations create a culture of ethics? Support your answer with real-world examples.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any EIGHT questions</p>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Distinguish between technical writing, academic writing, and creative writing. What are the unique characteristics that make technical writing essential in professional contexts?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">What is audience analysis? Explain how understanding your audience affects the purpose, scope, and medium of a technical document. Provide an example from IT industry.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">You are managing a mobile app development project. Create a detailed Gantt chart for a 12-week project including phases: requirement gathering (2 weeks), UI/UX design (2 weeks), development (5 weeks), testing (2 weeks), and deployment (1 week). Show dependencies and milestones.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Explain the copyediting and publishing phase of the writing process. What are the key differences between copyediting, proofreading, and peer review?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">Compare and contrast chronological resumes with functional resumes. When would you recommend using each type? Create a brief functional resume highlighting skills for a Technical Writer position.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">What is information architecture in web design? Describe the special considerations for writing different types of web pages: homepage, product page, and FAQ page.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Your company has developed a new cybersecurity software product. Write a persuasive news release (maximum 300 words) announcing this launch suitable for tech media outlets. Use the inverted pyramid structure.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Describe the key principles of designing effective graphics for technical documents. What factors should you consider when choosing between tables, bar charts, line graphs, flowcharts, and infographics? Provide examples for each type.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">13</span><span class="pyq-question-text">Your company has developed a new cybersecurity software product. Write a persuasive news release (maximum 300 words) announcing this launch suitable for tech media outlets. Use the inverted pyramid structure.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">14</span><span class="pyq-question-text">Define the following terms: a) White Paper b) Usability Testing c) Stakeholder Analysis d) Content Management System (CMS) e) Plain Language</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">15</span><span class="pyq-question-text">Write short notes on: a) Whistleblowing in technical communication b) Mechanism description versus process description</span><span class="pyq-marks">5</span></div>
          </div>
        </div>

        <!-- ===== 2081 Board ===== -->
        <a id="board-tw-2081"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>Technical Writing &mdash; 2081 Board</strong>
            <span class="pyq-meta">Full Marks: 80 + 20 &nbsp;|&nbsp; Pass Marks: 32 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any THREE questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Explain the role of audience analysis in technical writing and provide an example of how understanding the audience can affect the content and style of a technical document.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">You are now studying IT in a reputed campus under Tribhuvan University, Nepal. The campus has a well-equipped computer lab. You remember the school where you completed your secondary-level education. Most schools in Nepal have only a couple of desktop computers. You want to donate about a dozen computers to the school by raising funds. Write a letter to the Chief District Officer requesting him/her to permit you to collect donations. Include the specifications of the computers and the price list with the letter.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">Describe the structure and key components of a technical report. How does this structure enhance the report&rsquo;s effectiveness?</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">What are the ethical considerations in technical writing, and how can a writer ensure they adhere to ethical standards?</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any TEN questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Define FAQ, and draft five FAQs for your website.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">What is a Gantt chart? Make a Gantt chart of your assignment schedule.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">You have recently prepared an app. Compose a persuasive message in the AIDA method.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">What is the purpose of an executive summary in a technical document?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">How does technical writing differ from other forms of writing?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">Differentiate chronological resumes from functional resumes.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">What are the key steps in the technical writing process?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Why is peer review important in technical writing?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">13</span><span class="pyq-question-text">Describe the difference between a technical description and a technical definition.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">14</span><span class="pyq-question-text">Define the following terms: a) Pilot study b) Clinical research c) Alignment d) Stakeholder e) Rehearsing</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">15</span><span class="pyq-question-text">Write short notes on: a) Copy editing b) Whistleblowing</span><span class="pyq-marks">5</span></div>
          </div>
        </div>

        <!-- ===== 2080 Board ===== -->
        <a id="board-tw-2080"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>Technical Writing &mdash; 2080 Board</strong>
            <span class="pyq-meta">Full Marks: 80 + 20 &nbsp;|&nbsp; Pass Marks: 32 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any three questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Suppose you are working as an IT expert in the National Bank of Nepal, and working staff need five laptops for daily operation. Your manager asks you to present a proposal with time, cost, and objectives. Write a short proposal comparing the laptops available in the market of at least three renowned companies. Your proposal must include problems, solutions, and findings.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">As writing is not an overnight endeavor it follows a process. Discuss a process for technical writing.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">You have watched one of your peer&rsquo;s vlog (video blog) entries on the issue of &ldquo;Blocked mind as a malfunction of communication&rdquo;. What have you learned in addition to your ideas you learned from your teacher? How do your experiences in unblocking the mind differ from your peer? Write feedback to your peer&rsquo;s vlog.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">What are graphics? How are they used in technical writing?</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any ten questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Point out the differences between technical writing and academic writing.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">What is plagiarism? Why should we remain honest on borrowing other&rsquo;s ideas?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Compose an email to your immediate boss about the arrangements you have made for the upcoming IT fair at your campus premises.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">What issues should a web designer be concerned about when planning a web page?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">Construct a resume for the position of IT officer to apply in one of the companies in the US. In the resume present the candidate&rsquo;s professional ability to contribute to a new employment.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">Can you be a good friend with someone from another culture as with someone from your own culture? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Write a brief newspaper article on the opening of 25th Branch of Universal IT Solution in Pokhara headquarter.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Discuss the advantages of collaborative writing.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">13</span><span class="pyq-question-text">Make a flow-chart diagram of your dream application.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">14</span><span class="pyq-question-text">Imagine you are the manager of a company. You need to inform your staff that a new product is being launched on the occasion of New Year. Prepare a memo so that your staff understand and execute your plan.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">15</span><span class="pyq-question-text">Write short notes on: Zoom Presentation, Ethical Dilemma</span><span class="pyq-marks">5</span></div>
          </div>
        </div>

        <!-- ===== 2079 Board ===== -->
        <a id="board-tw-2079"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>Technical Writing &mdash; 2079 Board</strong>
            <span class="pyq-meta">Full Marks: 80 + 20 &nbsp;|&nbsp; Pass Marks: 32 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt all questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">What skills do you need to improve your technical writing? How can you acquire those skills?</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">How important is a collaborative effort in preparing documents? Discuss its advantages and disadvantages.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">What is effective communication? Elaborate on the principles of effective communication.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">&ldquo;The success with which you handle oral reporting may determine whether you are successful in your profession.&rdquo; Justify.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Think of the last time you worked on a group project with other people. What kind of experience did you have? What were the benefits of working with this group? What were the drawbacks? Write a short analysis.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Write a FAQ on how to get admission to B.Sc. CSIT at TU.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">If you are seeking a summer or part-time job, applying for admission to a school, or working on a project, write a progress report to the appropriate person about how you are accomplishing your goals.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Write news release for your college to announce an education fair.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">Suppose you have just completed the undergraduate degree (with a high GPA). Create a covert letter to apply for your dream job.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">You have to give a presentation on one of the occasions at college. Write a short speech on difficulty of being a student and employee.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Write a recommendation report to Kathmandu Metropolitian City in which you suggest an action that will improve waste management.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">13</span><span class="pyq-question-text">Write an e-mail that announces a new skill-oriented program at Shikhar IT Solutions. The program will allow workers to share each other&rsquo;s experience and grow together.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">14</span><span class="pyq-question-text">The Board of Directors of your company Nepal Distillery Ltd. has passed a proposal on providing bonus and incentives to all the employees. As a secretary of the company, you are responsible for informing the staff about the decision taken by the board meeting. Write a memo informing about the recently taken decision.</span><span class="pyq-marks">5</span></div>
          </div>
        </div>

        <!-- ===== 2078 Board ===== -->
        <a id="board-tw-2078"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>Technical Writing &mdash; 2078 Board</strong>
            <span class="pyq-meta">Full Marks: 80 + 20 &nbsp;|&nbsp; Pass Marks: 32 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any two questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Describe technical writing? Elaborate on its characteristics.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">&ldquo;Technical writing is written for both internal and external audiences.&rdquo; Justify with examples.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">What should one keep in mind when writing for the web? Discuss.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any eight questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">What is a press release? What steps should one follow to produce an effective press release?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Think of a subject or hobby about which you know a great deal. In a brief essay, describe how you acquired your knowledge.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Requesting him or her to increase incentives for the hardworking employees, write a letter to your employer.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Think of a time when something went wrong-perhaps a problem at college or work. After identifying and analyzing your audience, write an incident report describing the incident.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">You are working as the manager of an IT company. Write an email encouraging your staff to work for some additional hours every week so that the company and staff equally benefit.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">Write a press release for your school or another organization with which you are affiliated to announce an upcoming event, an accomplishment, or other newsworthy information.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">Based on your experience as an IT professional, write instructions for new aspirants, explaining how to begin a career in this field.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Write a chronological resume highlighting your skills for a job in your field.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Considering audience and purpose, write a short speech you are going to deliver in the inaugural session of the College IT Fair.</span><span class="pyq-marks">5</span></div>
          </div>
        </div>
      </div>
    </div>

    <a id="netcentric-notes"></a>
'''

# Find the Technical Writing PYQ section and replace it
# Look for the start of Technical Writing PYQ section
start_pattern = r'<div class="content-section">\s*<div class="content-header">\s*<a href="sem6\.html" class="back-link">&#8592; Back to Semester VI</a>\s*<h2>Technical Writing &mdash; Past Year Questions</h2>'

start_match = re.search(start_pattern, content)

# Find end - look for <a id="netcentric-notes"></a>
end_match = re.search(r'<a id="netcentric-notes"></a>', content)

if start_match and end_match:
    new_content = content[:start_match.start()] + new_tw_section
    with open(r'C:\Users\Ritesh Shrestha\toya-bsc-csit\sem6.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done! Technical Writing PYQ section updated with all 6 boards')
else:
    print(f'start_match: {start_match}')
    print(f'end_match: {end_match}')
