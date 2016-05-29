class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = ('id', 'description', 'format', 'timestamp', 'filename', 'filesize')