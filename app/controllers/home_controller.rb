class HomeController < ApplicationController

	def index
	end

	def boundary
		@lat = params[:lattitude]
		@lng = params[:longitude]
	end
	


end
