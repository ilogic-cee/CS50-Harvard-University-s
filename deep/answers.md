Random Partitioning
Will the observations likely be evenly distributed across all boats, even if AquaByte most commonly collects observations between midnight and 1 am? Why or why not?

The observations will not be evenly distributed. Random partitioning does not take into account the time of day when AquaByte collects most of its observations. Since AquaByte is most active between midnight and 1 am, there will likely be a higher concentration of observations during that time period. Randomly distributing the data across boats may result in some boats receiving more data than others.

Suppose a researcher wants to query for all observations between midnight and 1 am. On how many of the boats will they need to run the query?

The researcher will need to run the query on all of the boats. Since the data is randomly distributed, there is no guarantee that all observations between midnight and 1 am will be on a single boat. Therefore, the query needs to be executed on all boats to retrieve the relevant data.

Reasons to adopt this approach:

Simplicity: Random partitioning is a straightforward approach to distributing data, and it does not require complex logic for data assignment.
Load balancing: It can help distribute the load somewhat evenly across boats in terms of storage.
Reasons not to adopt this approach:

Inefficient queries: Random partitioning makes it challenging to retrieve specific time-based data efficiently, as queries may need to be executed on multiple boats.
Imbalanced data distribution: There is no guarantee that data will be evenly distributed, which can lead to storage imbalances and inefficient resource utilization.
Partitioning by Hour
Will the observations likely be evenly distributed across all boats, even if AquaByte most commonly collects observations between midnight and 1 am? Why or why not?

The observations will be evenly distributed. Partitioning by hour ensures that each boat is responsible for a specific time period, and since AquaByte's observations are spread across all hours of the day, the data will be evenly distributed among the boats.

Suppose a researcher wants to query for all observations between midnight and 1 am. On how many of the boats will they need to run the query?

The researcher will need to run the query on only one of the boats, specifically Boat C, which is responsible for storing observations from midnight to 1 am.

Reasons to adopt this approach:

Better query efficiency: Queries for specific time ranges are more efficient as the data is organized by time of day.
Clear data ownership: Each boat is responsible for a specific time period, making data ownership and management clear.
Reasons not to adopt this approach:

Imbalanced data distribution: Some boats may have significantly more data than others due to variations in observation frequency throughout the day.
Limited scalability: If AquaByte increases its observation frequency during a particular time period, the boat responsible for that period may become a bottleneck.
Partitioning by Hash Value
Will the observations likely be evenly distributed across all boats, even if AquaByte most commonly collects observations between midnight and 1 am? Why or why not?

The observations will likely be evenly distributed. Partitioning by hash value ensures that each observation is assigned a hash value based on its timestamp, distributing the data evenly across all possible hash values. Therefore, even if AquaByte collects most observations between midnight and 1 am, the hash function will ensure an even distribution.

Suppose a researcher wants to query for all observations between midnight and 1 am. On how many of the boats will they need to run the query?

The researcher will need to run the query on only one of the boats, as the hash value of the specific timestamp will determine the boat that holds the observation.

Suppose a researcher wants to query for a specific observation that occurred at exactly 2023-11-01 00:00:01.020. On how many of the boats will they need to run the query?

The researcher will need to run the query on only one of the boats, as the hash value of the specific timestamp will determine the boat that holds the observation.

Reasons to adopt this approach:

Even data distribution: Hash partitioning ensures an even distribution of data, preventing storage imbalances.
Scalability: The system can handle varying observation frequencies without becoming imbalanced.
Reasons not to adopt this approach:

Complexity: Implementing a hash function and managing hash values may introduce complexity to the system.
Query efficiency: Retrieving data for specific time ranges may still require querying multiple boats, depending on the hash function's distribution.
