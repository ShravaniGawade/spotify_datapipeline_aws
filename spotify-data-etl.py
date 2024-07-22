import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node artists
artists_node1720485417794 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-data-storage/staging/artists.csv"], "recurse": True}, transformation_ctx="artists_node1720485417794")

# Script generated for node track
track_node1720485419447 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-data-storage/staging/track.csv"], "recurse": True}, transformation_ctx="track_node1720485419447")

# Script generated for node albums
albums_node1720485416588 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-data-storage/staging/albums.csv"], "recurse": True}, transformation_ctx="albums_node1720485416588")

# Script generated for node albums-artists-join
albumsartistsjoin_node1720485915656 = Join.apply(frame1=albums_node1720485416588, frame2=artists_node1720485417794, keys1=["artist_id"], keys2=["id"], transformation_ctx="albumsartistsjoin_node1720485915656")

# Script generated for node track-join
trackjoin_node1720486073571 = Join.apply(frame1=track_node1720485419447, frame2=albumsartistsjoin_node1720485915656, keys1=["track_id"], keys2=["track_id"], transformation_ctx="trackjoin_node1720486073571")

# Script generated for node Drop Fields
DropFields_node1720486157216 = DropFields.apply(frame=trackjoin_node1720486073571, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1720486157216")

# Script generated for node target
target_node1720486178469 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1720486157216, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotify-data-storage/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="target_node1720486178469")

job.commit()