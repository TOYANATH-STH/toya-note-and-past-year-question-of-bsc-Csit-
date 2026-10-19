import re

with open(r'C:\Users\Ritesh Shrestha\toya-bsc-csit\sem6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New E-Governance PYQ section with all 6 boards
new_egov_section = '''    <div class="content-section">
      <div class="content-header">
        <a href="sem6.html" class="back-link">&#8592; Back to Semester VI</a>
        <h2>E-Governance &mdash; Past Year Questions</h2>
      </div>
      <div class="content-actions">
        <button class="btn btn-download">&#128466; Download PYQ PDF</button>
      </div>
      <div class="content-body">
        <!-- ===== 2082-new Board ===== -->
        <a id="board-egov-2082new"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2082-new Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Long Answer Questions (Attempt any TWO)</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">What are the present global trends of growth in E-Governance? Discuss with examples from developed and developing nations.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">What is a digital governance model? Describe the Critical Flow Model in E-Governance. How does it differ from other models?</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">What is the E-Governance maturity model? Explain the various maturity levels along with their characteristics.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Short Answer Questions (Attempt any EIGHT)</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Explain the importance of Cyber Laws in E-Governance.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">How can we use data warehousing and data mining concepts in agriculture and rural development?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Explain the concept of National Data Warehouses. How do they facilitate better governance?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Explain the E-governance security model.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">What is an Interoperability Framework? Why is it important?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">How can we achieve good governance through e-governance models?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">What is e-readiness? Discuss the data system infrastructural preparedness of e-readiness.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Describe any two E-Government initiatives in Nepal and their impact.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on:</span><span class="pyq-marks">5</span><p class="pyq-short-note">a. Cloud Governance</p><p class="pyq-short-note">b. E-Government Life Cycle</p></div>
          </div>
        </div>

        <!-- ===== 2082 Board ===== -->
        <a id="board-egov-2082"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2082 Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Long Answer Questions (Attempt any TWO)</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">What are the present global trends of growth in E-Governance? Discuss with examples from developed and developing nations.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">What is a digital governance model? Describe the Critical Flow Model in E-Governance. How does it differ from other models?</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">What is the E-Governance maturity model? Explain the various maturity levels along with their characteristics.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Short Answer Questions (Attempt any EIGHT)</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Explain the importance of Cyber Laws in E-Governance.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">How can we use data warehousing and data mining concepts in agriculture and rural development?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Explain the concept of National Data Warehouses. How do they facilitate better governance?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Explain the E-governance security model.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">What is an Interoperability Framework? Why is it important?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">How can we achieve good governance through e-governance models?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">What is e-readiness? Discuss the data system infrastructural preparedness of e-readiness.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Describe any two E-Government initiatives in Nepal and their impact.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on:</span><span class="pyq-marks">5</span><p class="pyq-short-note">a. Cloud Governance</p><p class="pyq-short-note">b. E-Government Life Cycle</p></div>
          </div>
        </div>

        <!-- ===== 2081 Board ===== -->
        <a id="board-egov-2081"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2081 Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; SECTION A</p>
            <p class="pyq-instruction">Attempt any TWO question.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">What are the benefits of using E-governance for both government and citizens? Why is it necessary to implement E-governance to provide government services to citizens efficiently? Explain with suitable example.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">Why is it necessary to use E-Government model? Explain interactive service model and critical flow model in detail.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">What different infrastructure are necessary to implement E-governance? Explain different computing infrastructure necessary to implement E-governance.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; SECTION B</p>
            <p class="pyq-instruction">Attempt any EIGHT question.</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">What is E-Governance? What is the scope of ICT implementation in government?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">What is the present global trends of growth in E-governance? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Explain realized level of E-Governance model in detail.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Discuss the impact and significance of E-Governance models while acheiving good governance.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Describe why human infrastructural preparedness and technological infrastructural preparedness are necessary in E-government.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">What is E-Governance security architecture? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">Discuss how data warehousing and data mining is used in census data.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">What is cyber law? How can we use this law to protect government data?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on:</span><span class="pyq-marks">5</span><p class="pyq-short-note">Cloud governance</p><p class="pyq-short-note">Data centers</p></div>
          </div>
        </div>

        <!-- ===== 2080 Board ===== -->
        <a id="board-egov-2080"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2080 Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any two questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Differentiate between e-governance and e-government. Explain the issues in e-governance implementations and how to solve these issues?</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">What do you mean by data warehousing and data mining? Explain the applications of data warehousing and data mining in census and prices of essential commodities.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">Explain broadcasting/wider dissemination model and comparative analysis model of e-governance with practical example.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any eight questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Explain in brief about scope and content of e-governance.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Discuss the important role of cyberlaw in Nepal.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">What do you mean by maturity levels of e-governance?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">Discuss the impact and significance of E-Governance models while acheiving good governance.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Describe why human infrastructural preparedness and technological infrastructural preparedness are necessary in E-government.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">Mention the existing scenario of e-governance in Nepal.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">What are different IT tools that are used to deliver services to citizens.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Discuss about the e-government security architecture.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on: (any two)</span><span class="pyq-marks">5</span><p class="pyq-short-note">Data system infrastructure</p><p class="pyq-short-note">Model of Digital governance</p><p class="pyq-short-note">Security standards.</p></div>
          </div>
        </div>

        <!-- ===== 2079 Board ===== -->
        <a id="board-egov-2079"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2079 Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any two questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Why is it necessary to implement E-Governance to provide government services to citizens efficiently and effectively? Explain using suitable example.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">Why do we need E-Government model? Explain interactive service model and critical flow model in detail.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">Why is it necessary to have IT infrastructure to implement E-Government? Explain different IT infrastructure needed to implement E-government.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any eight questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">&ldquo;E-Governance is to provide SMART government.&rdquo; Justify this statement .</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">What are the different stages of E-Government life cycle? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">What is E-Government maturity model? Describe the various maturity levels.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">How can we achieve good governance through E-Government models? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Define E-readiness. What is legal infrastructural preparedness?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">What are the challenges to E-Governance security? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">Explain the uses of data warehousing and data mining in agriculture.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Explain the E-Governance initiatives in Nepal?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on:</span><span class="pyq-marks">5</span><p class="pyq-short-note">a. E-government Security Architecture</p><p class="pyq-short-note">b.E-governance implementation in land reform</p></div>
          </div>
        </div>

        <!-- ===== 2078 Board ===== -->
        <a id="board-egov-2078"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2078 Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section A</p>
            <p class="pyq-instruction">Attempt any two questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Why do we need E-Governance? How can we use E-Governance to provide efficient services to citizens? Explain using suitable example.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">What is E-Governance model? Explain broadcasting/wider dissemination model and critical flow model in detail.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">Why do we need IT infrastructure to implement E-Governance? Explain network and computing infrastructure needed to implement E-governance.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Section B</p>
            <p class="pyq-instruction">Attempt any eight questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Define E-Government. Explain E-Government as an Information System.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">Why is it necessary to implement ICT in government? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">What is E-Government maturity model? Describe the various maturity levels.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">How can we achieve good governance through E-Government models? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Define E-readiness. What is data system infrastructural preparedness and technological infrastructural preparedness?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">What are different approaches to E-Governance security? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">Explain the uses of data warehousing and data mining in health, education and the rural development.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">How can we use human resource management software to support E-Government?  Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">Write short notes on:</span><span class="pyq-marks">5</span><p class="pyq-short-note">a. Electronic service delivery</p><p class="pyq-short-note">b. IT in judiciary</p></div>
          </div>
        </div>

        <!-- ===== 2076 Board ===== -->
        <a id="board-egov-2076"></a>
        <div class="pyq-board">
          <div class="pyq-year-header">
            <strong>E-Governance &mdash; 2076 Board</strong>
            <span class="pyq-meta">Full Marks: 60 + 20 + 20 &nbsp;|&nbsp; Pass Marks: 24 + 8 + 8 &nbsp;|&nbsp; Time: 3 Hours</span>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Group A</p>
            <p class="pyq-instruction">Attempt any two questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">1</span><span class="pyq-question-text">Differentiate between e-Government and e-Governance. What are the various stages of E-governance?</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">2</span><span class="pyq-question-text">Explain with example of maturity model of e-governance.</span><span class="pyq-marks">10</span></div>
            <div class="pyq-question"><span class="pyq-question-number">3</span><span class="pyq-question-text">Explain the components of data warehouse. What are the applications of data mining in eGovernance in the context of Nepal.</span><span class="pyq-marks">10</span></div>
          </div>
          <div class="pyq-section">
            <p class="pyq-section-title">&#10003; Group B</p>
            <p class="pyq-instruction">Attempt any eight questions.</p>
            <div class="pyq-question"><span class="pyq-question-number">4</span><span class="pyq-question-text">Explain the critical flow model in e-Governance.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">5</span><span class="pyq-question-text">What do you mean by e-Readiness framework? Explain with example.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">6</span><span class="pyq-question-text">Discuss the main impact of e-Governance application in digital divide.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">7</span><span class="pyq-question-text">What are the current trends of e-Governance development in Nepal.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">8</span><span class="pyq-question-text">Explain the Comparative Analysis Model with example.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">9</span><span class="pyq-question-text">What are the pre-requisites of e-readiness for intra structure development.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">10</span><span class="pyq-question-text">How can you develop the rural area through e-governance?</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">11</span><span class="pyq-question-text">Explain the strategic planning important for e-Government implementation.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">12</span><span class="pyq-question-text">What are the main contents are needed for human resource management software? Explain.</span><span class="pyq-marks">5</span></div>
            <div class="pyq-question"><span class="pyq-question-number">13</span><span class="pyq-question-text">Write short notes:</span><span class="pyq-marks">5</span><p class="pyq-short-note">a. IT in Judiciary</p><p class="pyq-short-note">b. E-Payment</p></div>
          </div>
        </div>
      </div>
    </div>

    <a id="netcentric-notes"></a>
'''

# Find where E-Governance PYQ section starts and ends
start_pattern = r'<div class="content-section">\s*<div class="content-header">\s*<a href="sem6\.html" class="back-link">&#8592; Back to Semester VI</a>\s*<h2>E-Governance &mdash; Past Year Questions</h2>'

start_match = re.search(start_pattern, content)

# Find the end - look for <a id="netcentric-notes"></a>
end_match = re.search(r'<a id="netcentric-notes"></a>', content)

if start_match and end_match:
    new_content = content[:start_match.start()] + new_egov_section + content[end_match.start():]
    with open(r'C:\Users\Ritesh Shrestha\toya-bsc-csit\sem6.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done! E-Governance PYQ section updated with all 6 boards')
else:
    print(f'start_match: {start_match}')
    print(f'end_match: {end_match}')
    print('Could not find section boundaries')
