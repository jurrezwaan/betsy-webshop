<center><div class="readability"><h1 id="assignment-betsy-webshop">Assignment: Betsy Webshop</h1>
<div class="wincpy">
<p><code class="interpreted-text" role="command">wincpy start d7b474e9b3a54d23bca54879a4f1855b</code></p>
</div>
<div class="prerequisites">
<p>You need to master the following to complete this assignment:</p>
<ul>
<li>Writing functions and function arguments;</li>
<li>SQL joins;</li>
<li>Database modelling;</li>
</ul>
</div>
<p>It is time to put all your SQL knowledge to the test. You will design a database for a fictional web marketplace called <strong>Betsy</strong>. Betsy is a site where people can
sell homemade goods. This assignment will test your skills in modelling data as well as using the <strong>peewee</strong> ORM. The requirements for this assignment can be split
into 2 parts: Modelling and Querying.</p>
<h2 id="modelling">Modelling</h2>
<p>Define your models and initialize the database in <code>models.py</code></p>
<p>A key part of the Betsy webshop is the database. At its core are the users and the products they offer:</p>
<blockquote>
<ul>
<li>A user has a name, address data, and billing information.</li>
<li>Each user must be able to own a number of products.</li>
<li>The products must have a name, a description, a price per unit, and a quantity describing the amount in stock.</li>
<li>The price should be stored in a safe way; rounding errors should be impossible.</li>
<li>In order to facilitate search and categorization, a product must have a number of descriptive tags.</li>
<li>The tags should not be duplicated.</li>
<li>We want to be able to track the purchases made on the marketplace, therefore a transaction model must exist</li>
<li>You can assume that only users can purchase goods</li>
<li>The transaction model must link a buyer with a purchased product and a quantity of purchased items</li>
</ul>
</blockquote>
<p>As a bonus requirement, you must consider the various constraints for all fields and incorporate these constraints in the data model.</p>
<h2 id="querying">Querying</h2>
<p>In order to manage the database, the webshop must have a number of querying utlities. The scaffolding for the utilities can be found in <code>main.py</code> Extend the methods
with the relevant functionality.</p>
<p>In this first iteration of the database we want to be able to:</p>
<blockquote>
<ul>
<li>Search for products based on a term. Searching for 'sweater' should yield all products that have the word 'sweater' in the name. This search should be case-insensitive</li>
<li>View the products of a given user.</li>
<li>View all products for a given tag.</li>
<li>Add a product to a user.</li>
<li>Remove a product from a user.</li>
<li>Update the stock quantity of a product.</li>
<li>Handle a purchase between a buyer and a seller for a given product</li>
</ul>
</blockquote>
<h2 id="test data">Test data</h2>
<p>To test if your database and queries are working we want to be able to populate the database with data quickly.</p>
<blockquote>
<ul>
<li>Add a <code>populate_test_database</code> function that fills the database with example data that works with your queries</li>
</ul>
</blockquote>
<p>In the next phase of development, the search functionality of the betsy webshop should be optimized. These requirements can be considered as a bonus:</p>
<blockquote>
<ul>
<li>The search should target both the name and description fields.</li>
<li>Additionally the products should be indexed so that the time spent on querying them is minimized.</li>
<li>Finally the search should account for spelling mistakes made by users and return products even if a spelling error is present</li>
</ul>
</blockquote></div></center>
