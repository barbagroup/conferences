I. Audience & Context Analysis
==============================
#### Speaking Goal: After my presentation is over, I want my audience to ...

I want my audience to be willing to give AmgXWrapper a try in their PETSc-based application, or, at least, try AmgX in their other applications.


##Audience Analysis
==============================

* *Who is your target audience?*
	* *Who do you most need to reach or impress?*
	* *What is their relationship to your topic?*

		1. They are who have existing PETSc-based applications and want to accelerate them by GPUs but don't want to do a lot of modifications or re-developing.
		2. Or they may have stopped developing their PETSc codes for a long time, but if they found an easy way to accelerate the programs, they are willing to try it on their old codes.

* *What are your audience's expectations for your presentation?*
	* *What do they hope to gain from the presentation?*
	* *What benefits might they get as a result?*

		1. How to use AmgXWrapper in their existing PETSc-based applications painlessly.
		2. Whether it is worth giving AmgX and AmgXWrapper a try.
		3. The performance of AmgX.
		4. The difference between AmgX and other GPU-based linear algebra libraries.

* *What knowledge does your audience have or need to have?*
	* *Do they know your organization, product/service, and terminology?*
	* *Do they know who you are and what you do?*

		1. PETSc and KSP solver; C/C++; MPI
		2. No, they don't know neither our organization and product nor who I am and what I do.

* *What are your audience members' attitude toward you and your message?*
	* *Are they receptive, favorable, neutral, apathetic, or hostile?*

	Neutral or maybe curious

* *What resistance does your audience have to you, your goal, or message?*
	* *What obstacles, biases, or experiences must be addressed?*

* *What questions might the audience ask?*
	* *What could be challenging, unclear, or incomplete?*

		Mathematical theories and algorithms in AmgX's multigrid preconditioners.


## Context
==============================

* *What is the timing of your presentation?*
	* *How long are you expected to speak*
	* *What will be occurring prior to your presentation and after*
	* *What time of day will you be speaking*

		25 minutes; 3:30 PM on the last day of conference

* *What is the physical setting of the location?*
	* *How many people will be present?*
	* *What technology is needed (mics, projectors, computers)?*
	* *How will people be seated (around a table/classroom style)?*
* *What is the tone of the event?*
	* *Is the situation formal or informal?*
	* *How should people feel at the end of your presentation?*
		
		1. Formal
		2. Intrigued
		


II. Structure Your Story
==============================

* Choice 1: What, So what, Now what?
* Choice 2: Problem-Solution?


III. Story Outline
==============================
#### Speaking Goal: After my presentation is over, I want my audience to ...

I want my audience to be willing to give AmgXWrapper a try in their PETSc-based application, or, at least, try AmgX in their other applications.

* **Key Point 1:** PETSc / PetIBM / AmgX
	* Poisson system costs most time in most CFD codes. Especially in PetIBM, it costs 90% of time, because the modified Poisson system is difficult to solve efficiently.
	* PETSc lacks GPU-support (does not support GPU very well)
	* It has been developed for several years. We don't want to spend much time on modifying codes, or even re-write the program for GPUs.
* **Key Point 2:** AmgXWrapper
	* The target => simple usage in PETSc-based application in order to ease the adopting AmgX
	* More MPI ranks than number of GPU devices: coarse level consolidation V.S. manual consolidation before calling AmgX => heterogeneous computing
	* lack of features
* **Key Point 3:** Performance of AmgXWrapper and its benefit
	* Benchmarks on pure Poisson system
	* Benchmarks on PetIBM
	* speed up and money saved


